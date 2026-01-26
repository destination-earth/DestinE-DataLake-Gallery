import os
import json

ISSUE_BODY_FILE = os.getenv("ISSUE_BODY_FILE", "issue_body.txt")
REGISTRY = os.getenv("REGISTRY_PATH", "cookbooks.json")  # repo root
TARGET_BRANCH = (os.getenv("TARGET_BRANCH") or "").strip().lower()  # "staging" or "main"

FIELDS = {
    "Repository URL": "",
    "Cookbook Title in capital letters": "",
    "Branch for STAGING preview": "",
    "Branch for MAIN (after promotion)": "",
}

def norm(s: str) -> str:
    return (s or "").strip().upper()

def load_issue_body() -> str:
    with open(ISSUE_BODY_FILE, encoding="utf-8") as f:
        return f.read()

def parse_fields(body: str) -> dict:
    lines = body.splitlines()
    current = None
    values = dict(FIELDS)

    for raw in lines:
        line = raw.strip().lstrip("#").strip()
        if line in values:
            current = line
            continue
        if current and line:
            values[current] = line.strip()
            current = None

    repo_url = (values["Repository URL"] or "").strip()
    root_path_raw = (values["Cookbook Title in capital letters"] or "").strip()
    staging_branch = (values["Branch for STAGING preview"] or "").strip()
    main_branch = (values["Branch for MAIN (after promotion)"] or "").strip()

    return {
        "repo_url": repo_url,
        "root_path_raw": root_path_raw,
        "root_path": norm(root_path_raw),
        "staging_branch": staging_branch,
        "main_branch": main_branch,
    }

def get_labels() -> set[str]:
    labels_raw = os.getenv("ISSUE_LABELS", "")
    return {x.strip() for x in labels_raw.split(",") if x.strip()}

def load_registry() -> list[dict]:
    if not os.path.exists(REGISTRY):
        return []
    try:
        with open(REGISTRY, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except Exception as e:
        print(f"WARNING: Could not read {REGISTRY} ({e}); using [].")
        return []

def save_registry(registry: list[dict]) -> None:
    with open(REGISTRY, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

def write_env(**kv) -> None:
    github_env = os.environ.get("GITHUB_ENV")
    if not github_env:
        print("WARNING: GITHUB_ENV not set; skipping env export.")
        return
    with open(github_env, "a", encoding="utf-8") as env_file:
        for k, v in kv.items():
            env_file.write(f"{k}={v}\n")

def pick_branch(staging_branch: str, main_branch: str) -> str:
    # Decide which branch to store into cookbooks.json
    if TARGET_BRANCH == "main":
        return (main_branch or "").strip()
    # default to staging behavior
    return (staging_branch or "").strip()

def main():
    if TARGET_BRANCH not in ("staging", "main"):
        # be forgiving: if not set, assume staging (preview)
        print(f"WARNING: TARGET_BRANCH='{TARGET_BRANCH}' not in (staging, main). Defaulting to 'staging'.")
        # local variable only, don't overwrite env
        chosen_target = "staging"
    else:
        chosen_target = TARGET_BRANCH

    body = load_issue_body()
    print("Full Issue Body:\n", body)

    fields = parse_fields(body)
    repo_url = fields["repo_url"]
    root_path_raw = fields["root_path_raw"]
    root_path = fields["root_path"]
    staging_branch = fields["staging_branch"]
    main_branch = fields["main_branch"]

    print("Extracted:")
    print("  repo_url        =", repo_url)
    print("  root_path_raw   =", root_path_raw)
    print("  root_path(norm) =", root_path)
    print("  staging_branch  =", staging_branch)
    print("  main_branch     =", main_branch)
    print("  TARGET_BRANCH   =", chosen_target)

    if not root_path:
        raise ValueError("ERROR: Root Path could not be extracted. Aborting.")

    labels = get_labels()
    print("ISSUE_LABELS:", sorted(labels))

    is_remove = "remove-repo" in labels
    is_add = ("add-repo" in labels) or ("promote-to-main" in labels)

    if is_add and is_remove:
        action = "remove"
    elif is_remove:
        action = "remove"
    elif is_add:
        action = "add"
    else:
        raise ValueError("No actionable label found.")

    branch_to_use = pick_branch(staging_branch, main_branch)

    write_env(COOKBOOK_ACTION=action, ROOT_PATH=root_path)
    if action == "add":
        if not repo_url:
            raise ValueError("ERROR: Repository URL is required for add/promote but is empty.")
        write_env(REPO_URL=repo_url, COOKBOOK_BRANCH=branch_to_use)

    registry = load_registry()

    before = len(registry)
    registry = [e for e in registry if norm(e.get("root_path")) != root_path]
    removed = before - len(registry)

    if action == "remove":
        print(f"Action=remove. Removed {removed} entries for root_path='{root_path}'.")
        save_registry(registry)
        return

    entry = {
        "repo_url": repo_url,
        "root_path": root_path,
    }

    if branch_to_use:
        entry["branch"] = branch_to_use

    registry.append(entry)
    save_registry(registry)

    print(f"Action=add. Upserted entry root_path='{root_path}' with branch='{branch_to_use or 'default'}'.")
    print("Registry root_paths now:", [norm(e.get("root_path")) for e in registry])

if __name__ == "__main__":
    main()

import os
import shutil
import subprocess
import tempfile
import json

# Aggregate repo providing HDA / HOOK / STACK
BASE_REPO = os.getenv("BASE_REPO", "https://github.com/destination-earth/DestinE-DataLake-Lab.git")

# Branch depends on gallery:
#   staging gallery => "staging"
#   main gallery    => "main"
BASE_REPO_BRANCH = os.getenv("BASE_REPO_BRANCH", "main")

BASE_CLONE_DIR = "cookbook-gallery"
PRODUCTION_DIR = "production"
CENTRAL_IMG = "img"

BASE_SUBFOLDERS = ["HDA", "HOOK", "STACK"]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, os.pardir))
REGISTRY = os.path.join(REPO_ROOT, "cookbooks.json")

def run(cmd):
    print("➜", " ".join(cmd))
    subprocess.run(cmd, check=True)

def clean_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)

def copytree_replace(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

def copy_images_into_central(repo_dir):
    src_img = os.path.join(repo_dir, "img")
    if not os.path.isdir(src_img):
        return

    os.makedirs(CENTRAL_IMG, exist_ok=True)

    for name in os.listdir(src_img):
        s = os.path.join(src_img, name)
        d = os.path.join(CENTRAL_IMG, name)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

    print(f"Copied images from {src_img} → {CENTRAL_IMG}")

def find_subfolder(repo_root, sub):
    candidates = [
        os.path.join(repo_root, "production", sub),
        os.path.join(repo_root, sub),
    ]
    for c in candidates:
        if os.path.isdir(c):
            return c
    return None

def sync_base_sections():
    print(f"Cloning aggregate repo: {BASE_REPO} (branch: {BASE_REPO_BRANCH})")

    run([
        "git", "clone",
        "--depth", "1",
        "--single-branch",
        "--branch", BASE_REPO_BRANCH,
        BASE_REPO,
        BASE_CLONE_DIR
    ])

    for sub in BASE_SUBFOLDERS:
        src = find_subfolder(BASE_CLONE_DIR, sub)
        dst = os.path.join(PRODUCTION_DIR, sub)

        if src:
            print(f"Updating section from aggregate repo: {dst}")
            copytree_replace(src, dst)
        else:
            print(f"Skipping {sub}: not found in aggregate repo")

    copy_images_into_central(BASE_CLONE_DIR)

def sync_external_cookbooks():
    print("Looking for registry at:", REGISTRY)
    print("Exists:", os.path.exists(REGISTRY))
    if not os.path.exists(REGISTRY):
        print("No cookbooks.json found — skipping external cookbooks.")
        return

    try:
        with open(REGISTRY, "r", encoding="utf-8") as f:
            items = json.load(f)
    except Exception as e:
        print(f"Could not parse cookbooks.json: {e}")
        return

    if not isinstance(items, list) or not items:
        print("cookbooks.json is empty — no external cookbooks.")
        return

    with tempfile.TemporaryDirectory() as tmp:
        for it in items:
            repo_url = (it.get("repo_url") or "").strip()
            root = (it.get("root_path") or "").strip()
            branch = (it.get("branch") or "").strip()

            if not repo_url or not root:
                print(f"Invalid entry in cookbooks.json: {it}")
                continue

            print(f"Sync external cookbook: {root} from {repo_url} (branch: {branch or 'default'})")

            repo_tmp = os.path.join(tmp, root)

            clone_cmd = ["git", "clone", "--depth", "1"]
            if branch:
                clone_cmd += ["--single-branch", "--branch", branch]
            clone_cmd += [repo_url, repo_tmp]
            run(clone_cmd)

            dst = os.path.join(PRODUCTION_DIR, root)
            copytree_replace(repo_tmp, dst)

            # remove .git
            git_dir = os.path.join(dst, ".git")
            if os.path.isdir(git_dir):
                shutil.rmtree(git_dir)

            # move images to central img/ folder
            copy_images_into_central(repo_tmp)

            # remove img folder from production copy
            img_in_production = os.path.join(dst, "img")
            if os.path.isdir(img_in_production):
                shutil.rmtree(img_in_production)

    print("All external cookbooks synced.")

def main():
    if os.path.exists(PRODUCTION_DIR):
        shutil.rmtree(PRODUCTION_DIR)

    os.makedirs(PRODUCTION_DIR, exist_ok=True)
    sync_base_sections()
    sync_external_cookbooks()
    clean_dir(BASE_CLONE_DIR)

if __name__ == "__main__":
    main()

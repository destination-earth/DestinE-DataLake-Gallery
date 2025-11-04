import os
import nbformat
import yaml

PRODUCTION_ROOT = "production"
START_MARKER = "### Filter Notebooks by Tags"
BUTTON_PREFIX = "{button}`"
BUTTON_SUFFIX = "`"

def extract_yaml_from_notebook(notebook_path):
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            content = cell.source.strip()
            if content.startswith("---") and content.count("---") >= 2:
                parts = content.split("---")
                yaml_block = parts[1]
                try:
                    return yaml.safe_load(yaml_block)
                except yaml.YAMLError as e:
                    print(f"YAML parsing error in {notebook_path}: {e}")
                    return None
            break
    return None


def collect_unique_tags():
    unique_tags = set()
    for dirpath, _, filenames in os.walk(PRODUCTION_ROOT):
        for filename in filenames:
            if filename.endswith(".ipynb"):
                full_path = os.path.join(dirpath, filename)
                meta = extract_yaml_from_notebook(full_path)
                if meta and "tags" in meta:
                    for tag in meta["tags"]:
                        if isinstance(tag, str):
                            unique_tags.add(tag.strip())
   
    return sorted(unique_tags, key=lambda s: s.lower())


def make_buttons_block(tags):
    return [
        f"{BUTTON_PREFIX}{tag} <galleries_by_tag/tag-{tag.replace(' ', '-').replace('/', '-')}.md>{BUTTON_SUFFIX}\n"
        for tag in tags
    ]


def update_file(file_path, buttons):
    if not os.path.isfile(file_path):
        print(f"{file_path} not found, skipping.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    try:
        marker_idx = next(i for i, ln in enumerate(lines) if ln.strip() == START_MARKER)
    except StopIteration:
        print(f"Marker '{START_MARKER}' not found in {file_path}, skipping.")
        return

    start_idx = marker_idx + 1
    if start_idx < len(lines) and lines[start_idx].strip() == "":
        start_idx += 1

    end_idx = start_idx
    while end_idx < len(lines):
        s = lines[end_idx].strip()
        if not s:
            end_idx += 1
            continue
        if s.startswith(BUTTON_PREFIX) and s.endswith(BUTTON_SUFFIX):
            end_idx += 1
            continue
        break

    replacement = ["\n"] + buttons + ["\n"]
    new_lines = lines[:start_idx] + replacement + lines[end_idx:]

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"Updated buttons in {file_path}")


if __name__ == "__main__":
    tags = collect_unique_tags()

    buttons_block = make_buttons_block(tags)
    update_file("index.md", buttons_block)

import os
import nbformat
import yaml

PRODUCTION_ROOT = "production"
TAG_GALLERY_DIR = "galleries_by_tag"
GALLERY_DIRS = ["galleries", "galleries_by_tag"]
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
                yaml_block = content.split("---")[1]
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


def make_buttons_block(tags, base_dir="."):
    rel_to_tags = os.path.relpath(TAG_GALLERY_DIR, start=base_dir or ".")
    buttons = []
    for tag in tags:
        tag_file = f"tag-{tag.lower().replace(' ', '-').replace('/', '-')}.md"
        link_path = os.path.join(rel_to_tags, tag_file).replace(os.sep, "/")
        buttons.append(f"{BUTTON_PREFIX}{tag} <{link_path}>{BUTTON_SUFFIX}\n")
    return buttons


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
    while start_idx < len(lines) and not lines[start_idx].strip():
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

    buttons_block = make_buttons_block(tags, base_dir=".")
    update_file("index.md", buttons_block)

    for gallery_dir in GALLERY_DIRS:
        if not os.path.isdir(gallery_dir):
            continue
        for md_file in os.listdir(gallery_dir):
            if md_file.endswith(".md"):
                base_dir = os.path.dirname(os.path.join(gallery_dir, md_file))
                buttons_block = make_buttons_block(tags, base_dir)
                update_file(os.path.join(gallery_dir, md_file), buttons_block)

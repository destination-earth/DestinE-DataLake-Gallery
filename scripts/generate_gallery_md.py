import os
import nbformat
import yaml
import shutil

PRODUCTION_ROOT = "production"
GALLERY_DIR = "galleries"
SECTIONS = [d for d in os.listdir(PRODUCTION_ROOT) if os.path.isdir(os.path.join(PRODUCTION_ROOT, d))]


if os.path.exists(GALLERY_DIR):
    shutil.rmtree(GALLERY_DIR) 

os.makedirs(GALLERY_DIR, exist_ok=True)

def extract_yaml_from_notebook(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            content = cell.source.strip()
            if content.startswith('---') and content.count('---') >= 2:
                parts = content.split('---')
                yaml_block = parts[1]
                try:
                    return yaml.safe_load(yaml_block)
                except yaml.YAMLError as e:
                    print(f"YAML parsing error in {notebook_path}: {e}")
                    return None
            break
    return None

def wrap_gallery_cards(cards_html):
    return f'''### Filter Notebooks by Tags
<div style="display: flex; flex-direction: column; gap: 20px; max-width: 800px;">
{chr(10).join(cards_html)}
</div>
'''.strip()

def generate_html_card(meta, notebook_path):
    title = meta.get("title", "Untitled")
    subtitle = meta.get("subtitle") or "no description"
    tags = meta.get("tags", [])
    tags_html = ''.join(f'<span class="tag">{tag}</span>' for tag in tags)

    # Root-relative notebook link (robust for GitHub Pages + baseurl)
    href = "/" + notebook_path.replace("\\", "/").lstrip("./")

    thumbnail = (meta.get("thumbnail") or "").strip()

    # Normalize thumbnails:
    # - if metadata contains "img/..." or "/img/..." -> turn into "/img/..."
    # - if empty -> keep empty
    if thumbnail:
        thumb_norm = thumbnail.replace("\\", "/").lstrip("./")
        if thumb_norm.startswith("/img/"):
            thumbnail = thumb_norm
        elif thumb_norm.startswith("img/"):
            thumbnail = "/" + thumb_norm
        elif "img/" in thumb_norm:
            # e.g. "something/img/foo.png"
            thumbnail = "/img/" + thumb_norm.split("img/", 1)[1].lstrip("/")
        else:
            # If someone gave a direct path, still make it root-relative
            thumbnail = "/" + thumb_norm.lstrip("/")

    return f'''
<div class="notebook-card" data-tags="{' '.join(tags)}" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
  <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
    <img src="{thumbnail}" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
  </div>
  <div style="flex: 1;">
    <strong>{title}</strong><br>
    {subtitle}
    <div style="margin: 6px 0;">
      {tags_html}
    </div>
    <a href="{href}" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
  </div>
</div>
'''.strip()



def generate_gallery_for_section(section):
    section_path = os.path.join(PRODUCTION_ROOT, section)
    output_md = os.path.join(GALLERY_DIR, f"{section}.md")
    cards = []

    for dirpath, _, filenames in os.walk(section_path):
        for filename in sorted(filenames):
            if filename.endswith(".ipynb"):
                full_path = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(full_path, ".")
                meta = extract_yaml_from_notebook(full_path)
                if meta:
                    card = generate_html_card(meta, rel_path)
                    cards.append(card)
                else:
                    print(f"No metadata found in {full_path}")

    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(f"# {section} Gallery\n\n")
        wrapped_html = wrap_gallery_cards(cards)
        f.write(wrapped_html)

    print(f"{output_md} created with {len(cards)} cards.")


if __name__ == "__main__":
    for section in SECTIONS:
        generate_gallery_for_section(section)


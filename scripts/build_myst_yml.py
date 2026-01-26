import yaml
import os

if os.path.exists("myst.yml"):
    os.remove("myst.yml")

PRODUCTION_ROOT = "production"
main_sections = [d for d in os.listdir(PRODUCTION_ROOT) if os.path.isdir(os.path.join(PRODUCTION_ROOT, d))]

BASE_URL = os.getenv("BASE_URL", "").rstrip("/")
# optional safety: ensure it starts with /
if BASE_URL and not BASE_URL.startswith("/"):
    BASE_URL = "/" + BASE_URL
    
toc = [
    {"file": "index.md"},
    {"title": "Contribute", 
     "file": "contribute.md"},
]

for section in main_sections:
    entry = {
        "title": section,
        "file": f"galleries/{section}.md",
        "children": []
    }

    section_path = os.path.join(PRODUCTION_ROOT , section)
    for dirpath, _, filenames in os.walk(section_path):
        for f in sorted(filenames):
            if f.endswith(".ipynb"):
                full_path = os.path.join(dirpath, f)
                rel_path = os.path.relpath(full_path, ".").replace("\\", "/")
                entry["children"].append({"file": rel_path,
                                         "hidden": True,})
    toc.append(entry)

tag_gallery_dir = "galleries_by_tag"
if os.path.exists(tag_gallery_dir):
    for fname in sorted(os.listdir(tag_gallery_dir)):
        if fname.endswith(".md"):
            toc.append({
                "file": f"{tag_gallery_dir}/{fname}",
                "hidden": True,
            })

config = {
    "version": 1,
    "project": {
        "title": "DEDL Notebook Gallery",
        "toc": toc,
        "baseurl": BASE_URL,
    },
    "site": {
        "template": "book-theme",
        "options": {
            "style": "_static/custom.css",
            "favicon": "img/EUMETSAT-icon.ico",
            "logo": "img/logo_bar.png",
            "hide_footer_links": True,
            "hide_outline": True
        },
        "parts": {
            "footer": "footer.md"
        }
    }
}

with open("myst.yml", "w", encoding="utf-8") as f:
    yaml.dump(config, f, sort_keys=False)

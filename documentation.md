# DEDL Notebook Gallery Setup und Configuration

The DEDL Gallery Website provides a structured overview of all available notebooks in Destination Earth-DataLake grouped into three core services: HOOK, STACK, and HDA. This document explains how the site is set up, how it works, and how to modify or extend its configuration.

Below is a breakdown of each major directory in
[https://github.com/destination-earth/DestinE-DataLake-Gallery.git](https://github.com/destination-earth/DestinE-DataLake-Gallery.git)
and its purpose, followed by a step-by-step tutorial on how to contribute.

# Files and Folder Structure (Gallery Repository)

## 1. `_static/`

Contains `custom.css`, which defines the visual appearance of the gallery:

* colors
* fonts
* spacing
* layout styles

You can freely edit this file. Changes are included automatically in the next gallery build.

## 2. `img/`

Contains all images used by the gallery and notebooks.

Important:

* **Do not** upload notebook thumbnails directly to the gallery repo.
* Internal notebook images belong in the **LAB repository’s** `img/` folder.
* External notebook images belong in the **external repository’s** `img/` folder.

All images are automatically copied into this folder when the gallery is built.

## 3. `scripts/`

These Python scripts automate the entire gallery generation pipeline.

### `clone_sync_repos.py`

Clones the LAB repository (`main`) and copies:

* `HDA/`, `HOOK/`, `STACK/` → into `production/`
* All images from LAB → into `img/`

It also reads the `cookbooks.json` file stored in the LAB repository.
For each external entry, the script:

* clones the external repository
* copies its notebooks into `production/`
* copies its `img/` folder into the gallery’s `img/` folder

Thus, **all internal and external notebooks are synchronized** during each build.

### `generate_gallery_md.py`

Generates gallery pages (one per subfolder in `production/`).

It extracts notebook metadata (title, subtitle, tags, thumbnail) from the first markdown cell and renders an HTML-based notebook card.

Output goes into `galleries/`.

### `generate_keywords.py`

Scans all notebooks for tags and creates tag-based gallery pages.

Output goes into `galleries_by_tag/`.

### `indexbutton.py`

Updates `index.md` and all gallery pages with the global list of tag filter buttons.
It replaces the content below the marker:

```
### Filter Notebooks by Tags
```

### `build_myst_yml.py`

Generates the `myst.yml` configuration dynamically.

This file defines:

* navigation
* theme settings
* index, contribute, footer pages
* all notebook pages in `production/`

Because the script regenerates `myst.yml`, **manual edits should not be made**.

## Additional Files (Gallery)

### `myst.yml`

The MyST website configuration, fully auto-generated.

### `footer.md`

Footer content displayed at the bottom of each page.

### `contribute.md`

Short overview on contributing.

# Gallery Workflow

## `build_myst_page.yml`

**Gallery Build Workflow**

Triggered on:

* every push to `main`
* manual dispatch
* every 2 hours

Steps:

1. Clone LAB repository (`main`)
2. Synchronize internal and external notebooks (`clone_sync_repos.py`)
3. Generate gallery pages (`generate_gallery_md.py`)
4. Generate tag pages (`generate_keywords.py`)
5. Insert tag filter buttons (`indexbutton.py`)
6. Generate `myst.yml` (`build_myst_yml.py`)
7. Build HTML
8. Deploy to GitHub Pages

This workflow builds the [public production gallery](https://destination-earth.github.io/DestinE-DataLake-Gallery/)

---

# Files and Folder Structure (LAB Repository)

## 1. `.github/ISSUE_TEMPLATE/`

Contains the issue form “Add new cookbook”.
Used by external contributors to add new notebook repositories.

The form collects:

* repository URL
* short uppercase folder name

## 2. `.github/workflows/integrate_cookbook.yml`

**External Repository Integration Workflow**

Triggered when:

* an issue is closed in the LAB repository, and
* the actor is an approved maintainer

Steps:

1. Save issue body to `issue_body.txt`
2. Parse the submitted form (`parse_issue.py`)
3. Clone external repository
4. Validate all notebooks (YAML metadata)
5. Update `cookbooks.json`
6. Commit changes to **LAB/staging**

External entries therefore always enter STAGING first.

Once STAGING is reviewed and merged into MAIN, the gallery rebuilds automatically.

## 3. `.github/workflows/pr_check.yml`

Triggered for Pull Requests to LAB/staging and LAB/main.

The workflow verifies:

* metadata in first notebook cell
* required fields (title, subtitle, thumbnail, tags, etc.)
* validity of notebook structure

Only PRs whose notebooks pass validation can be merged.

---

# How to contribute

You can either:

1. Add a new notebook to an existing section (HDA, HOOK, STACK), or
2. Propose a completely new notebook section (external repository).


# Adding a notebook to an existing section

### Step 1: Use the official notebook template

[https://github.com/destination-earth/DestinE-DataLake-NotebookTemplate/blob/main/notebooks/template.ipynb](https://github.com/destination-earth/DestinE-DataLake-NotebookTemplate/blob/main/notebooks/template.ipynb)

Make sure the first cell contains correctly formatted YAML metadata.

### Step 2: Create a Pull Request to the **staging branch of the LAB repository**

Place:

* your notebook into `HDA/`, `HOOK/`, or `STACK/`
* images into the LAB repository’s `img/` directory

LAB repository:
[https://github.com/destination-earth/DestinE-DataLake-Lab/tree/staging](https://github.com/destination-earth/DestinE-DataLake-Lab/tree/staging)

A validation workflow checks:

* metadata format
* required fields
* thumbnail references

### Step 3: Preview in the staging gallery

After a successful PR, the staging version of the gallery is built. 
You can verify the layout, metadata, tags, and images.

### Step 4: Promote to main

Once approved, the PR from `staging` to `main` is created.
Only maintainers may approve and merge this step.

The main branch update triggers the public gallery rebuild.


# Adding a new yection (external repository)

If you want to add an entirely new notebook repository:

### Step 1: Use the Template Repository

Clone or copy:

[https://github.com/destination-earth/DestinE-DataLake-NotebookTemplate](https://github.com/destination-earth/DestinE-DataLake-NotebookTemplate)

Your repository must contain:

```
notebooks/
img/
```

### Step 2: Add your notebooks and images

* All notebooks must follow the template, including YAML metadata.
* All images must go into the local `img/` folder.

### Step 3: Submit your repository via issue form

Open the “Add new cookbook” submission form:

https://github.com/destination-earth/DestinE-DataLake-Lab/issues/new/choose

Provide:

* Submision Title
* Repository URL
* Short uppercase folder name (used in the gallery structure)

### Step 4: Maintainer closes the issue

Only approved maintainers can do this.

Closing the issue triggers:

* Parsing the issue input
* Cloning the external repository
* Validating the notebooks
* Updating `cookbooks.json` in LAB/staging
* Building the staging-Gallery for validation

### Step 5: Promotion to main

A PR from staging → main is created or reviewed by maintainers.

### Step 6: Automatic gallery integration

Once LAB/main updates, the Gallery repository rebuilds and the new section appears.

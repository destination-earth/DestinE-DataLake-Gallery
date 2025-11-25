# DEDL Notebook Gallery Setup und Configuration

The DEDL Gallery Website provides a structured overview of all available notebooks in Destination Earth-DataLake grouped into three core services: HOOK, STACK, and HDA. This document explains how the site is set up, how it works, and how to modify or extend its configuration.

Below is a breakdown of each major directory in [DestinE-DataLake-Gallery](https://github.com/destination-earth/DestinE-DataLake-Gallery.git) and of the [DestinE-DataLake-Lab Repository](https://github.com/destination-earth/DestinE-DataLake-Lab) and its purpose, followed by a step-by-step tutorial on how to contribute.

# Files and Folder Structure (Gallery Repository)

## 1. `_static/`

The `custom.css` file defines the visual appearance of the site, including colors, font styles, spacing, and header size.

To make design changes (e.g., colors, fonts), you can directly edit custom.css. These changes will be automatically applied with every push, without additional steps required.

## 2. `img/`

This folder contains all images used by the notebooks or the website itself. When adding a new notebook, you can include a thumbnail image and reference it in the first Markdown cell. You do not need to include your images in here, this will be handled automatically when you add you images to the img/ folder in de DestinE-Datalake-Lab repo. 

For further information please have a look at the the Contributing section below!

## 3. `scripts/`

These Python scripts automate the entire gallery generation pipeline.

### `clone_sync_repos.py`

Clones the current version of the repository https://github.com/destination-earth/DestinE-DataLake-Lab.git (branch: main) and copies:

* `HDA/`, `HOOK/`, `STACK/` → into `production/`
* All images from LAB → into `img/`

It also reads the `cookbooks.json` file stored in the LAB repository.
For each external entry, the script:

* clones the external repository
* copies its notebooks into `production/`
* copies its `img/` folder into the gallery’s `img/` folder

Thus, **all internal and external notebooks are synchronized** during each build.

### `generate_gallery_md.py`

Generates a gallery page for each subfolder within `production/`.
It extracts metadata (title, description, tags) from the first Markdown cell of each notebook and creates a gallery card using HTML <div> blocks.

Generated gallery pages are stored in the `galleries/` folder.

**Note:** To adjust the card design, edit the corresponding HTML layout directly in this script.

### `generate_keywords.py`

Creates tag‑specific gallery pages by scanning the first Markdown cell of each notebook, extracting the tags, and generating one gallery per tag.
The resulting pages are stored in the galleries_by_tag/ folder.

### `indexbutton.py`

Automatically updates index.md and all gallery markdown files by inserting or replacing a section of tag filter buttons.
It scans the galleries_by_tag/ folder and generates corresponding {button} links.

The script locates the marker ### Filter Notebooks by Tags in each file and replaces the section below it with the updated tag buttons — keeping all gallery pages synchronized with new tags automatically.

### `build_myst_yml.py`

Generates the `myst.yml` configuration dynamically.

This file defines:

* navigation
* theme settings
* index, contribute, footer pages
* all notebook pages in `production/`

**Note:** Any structural changes to the site (navigation, theme, or appearance) must be made in this script — not directly in myst.yml, since that file is dynamically generated here

## Additional Files (Gallery)

### `myst.yml`

This file defines the structure and configuration of the MyST site.
It is automatically generated and updated by the script build_myst_yml.py.

### `footer.md`

Contains the footer content that appears on every page of the gallery.
You can easily modify or extend it if you want to update contact details or design elements.

### `contribute.md`

Provides contribution guidelines similar to the “How to Contribute” section in this documentation.
You can update it to reflect new submission rules or workflow instructions.

# Gallery Workflow

## `.github/workflow/build_myst_page.yml`

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

# Staging Gallery

The [DestinE-staging-Gallery](https://github.com/destination-earth/DestinE-Staging-Gallery.git) is designed exactly the same way, however it clones the staging brnah of the LAB repository, not the main branch.
---

# Files and Folder Structure (LAB Repository)

## 1. `.github/ISSUE_TEMPLATE/`

Contains the issue form “Add new cookbook”.
Used by external contributors to add new notebook repositories.

The form collects:

* Submission Title 
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

External entries therefore always enter STAGING first. You cna have a look at the Staging Gallery then. 

Once STAGING is reviewed and merged into MAIN, the gallery gets updated (every two hours).

## 3. `.github/workflows/pr_check.yml`

Triggered for Pull Requests to LAB/staging and LAB/main.

The workflow verifies:

* metadata in first notebook cell
* required fields (title, subtitle, thumbnail, tags, etc.)

Only PRs whose notebooks pass validation will be merged.

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

### Step 3: Preview in the staging gallery

After a successful PR, the staging version of the gallery is built. 
You can verify the layout, metadata, tags and images.

### Step 4: Promote to main

Once approved, the PR from `staging` to `main` is created.
Only maintainers may approve and merge this step.

The public gallery is rebuild from the main branch every 2 hours.

# Adding a new section (external repository)

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

# DEDL Notebook Gallery SetUp und Confuguration

The **DEDL Notebook Gallery** provides a structured overview of all available notebooks in the Destination Earth Data Lake, grouped into the three core services **HDA**, **HOOK**, and **STACK**.  
This document explains how the gallery is structured, how it is built, and how it can be extended or modified.

It covers the

- **Gallery repository**  
    [https://github.com/destination-earth/DestinE-DataLake-Gallery](https://github.com/destination-earth/DestinE-DataLake-Gallery)  

- **Staging Gallery repository**
    [https://github.com/destination-earth/DestinE-DataLake-Staging-Gallery](https://github.com/destination-earth/DestinE-DataLake-Staging-Gallery)
    
- **LAB repository**  
    [https://github.com/destination-earth/DestinE-DataLake-Lab](https://github.com/destination-earth/DestinE-DataLake-Lab)
    
and explains how they interact.
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

The public gallery is rebuild from the main branch.

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
* All images must go into the `img/` folder.

### Step 3: Submit your repository via issue form

Open the “Add new cookbook” submission form:

https://github.com/destination-earth/DestinE-DataLake-Gallery/issues

Provide:

* Submision Title
* Repository URL
* Short uppercase folder name (used in the gallery structure)
* Branch from which the staging Gallery should be build from
* Branch from which the main-Gallery should be build from

### Step 4: issue gets label = add-repo

Once the issue is opened, it gets the label 'add-repo' and gets automatically included into the staging gallery, visible via: https://destination-earth.github.io/DestinE-DataLake-Staging-Gallery/

### Step 4: Maintainer chooses to approve or remove the Repository

Only approved maintainers can do this. Adding the label promote-to-main triggers an automatic workflow that allows the issue repository to be included into the main gallery.

Note:  
If a repository has already been promoted to the main gallery and should be removed completely:
1. Apply the label `remove-repo`  
   → removes it from the staging gallery
2. AND Apply the label `promote-to-main`  
   → propagates the removal to the main gallery


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

This script performs the **core synchronization step** of the gallery build.

It:

- clones the LAB repository  
    `https://github.com/destination-earth/DestinE-DataLake-Lab.git`
- checks out the branch defined via `BASE_REPO_BRANCH` (typically `main` or `staging`)
- copies:
    
    - `HDA/`, `HOOK/`, `STACK/` → into `production/`       
    - all images → into the gallery’s `img/` folder
        

Additionally, the script reads `cookbooks.json`.

For each external cookbook entry it:

- clones the external repository (using the configured branch)
- copies its notebooks into `production/<ROOT_PATH>/`
- copies its `img/` folder into the gallery’s central `img/` directory
    

As a result, **all internal and external notebooks are synchronized on every build**

### `generate_gallery_md.py`

Generates one gallery page per subfolder in `production/`.
For each notebook, it:

- extracts metadata (title, subtitle, tags) from the **first Markdown cell**
- renders a gallery card using HTML `<div>` blocks
    

The generated pages are stored in `galleries/`.
**Note:**  
To change the layout or appearance of gallery cards, edit the HTML template directly in this script.

### `generate_keywords.py`

Creates **tag-based gallery pages**.

It:
- scans all notebooks in `production/`
- extracts tags from the first Markdown cell
- generates one gallery page per tag
    
The resulting pages are stored in `galleries_by_tag/`

### `indexbutton.py`

Automatically inserts or updates the **tag filter buttons** on:

- `index.md`
- all gallery pages

The script:
- scans `galleries_by_tag/`
- generates `{button}` links for each tag
- replaces the section below the marker  
    `### Filter Notebooks by Tags`
    
This keeps all tag filters synchronized automatically.

### `build_myst_yml.py`

Dynamically generates the `myst.yml` configuration file.
It defines:

- navigation structure
- theme configuration
- index, contribute, and footer pages
- all notebook pages from `production/`
    
**Important:**  
Structural or layout changes **must be done in this script**, not directly in `myst.yml`, as that file is regenerated on every build.

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

# Gallery Workflows

## 1. `.github/workflow/build_myst_page.yml`

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

## 2. `.github/workflow/build_myst_page_staging.yml`

Uses the same steps as the production workflow, but:

- builds from the `staging` branch
- includes unreviewed external cookbooks
- deploys to a **separate GitHub Pages target**

Used for preview and review before promotion to `main`.

Staging Gallery can be accessed via: https://destination-earth.github.io/DestinE-DataLake-Staging-Gallery/
## 4 `.github/workflows/integrate_cookbook.yml`

Triggered when:

- an issue titled **“Add external cookbook”** has the label **`add-repo`** or **`remove-repo`**
- the actor is an approved maintainer

Steps:

1. Save the issue body
2. Parse the submission (`parse_issue.py`)
3. Clone the external repository
4. Validate all notebooks (YAML metadata)
5. Update `cookbooks.json` on the **staging** branch

All external cookbooks **always enter STAGING first** and are only included in the production gallery after review and promotion.

## 5 `.github/workflows/promote_to_main.yml`

Triggered when:
- an issue titled **“Add external cookbook”** has the label **`promote-to-main`** 

Promotes a reviewed external cookbook from **staging** to **main** by:

- re-processing the issue
- updating `cookbooks.json` in `main`
- triggering a new production build

## 6 `.github/ISSUE_TEMPLATE/submit_repo.yml`

Contains the issue form “Add new cookbook”.
Used by external contributors to add new notebook repositories.

The form collects:

Provide:

* Submission Title
* Repository URL
* Short uppercase folder name (used in the gallery structure)
* Branch from which the staging Gallery should be build from
* Branch from which the main-Gallery should be build from

# DEDL Notebook Gallery Setup und Configuration

The DEDL Gallery Website provides a structured overview of all available notebooks in Destination Earth-DataLake grouped into three core services: HOOK, STACK, and HDA. This document explains how the site is set up, how it works, and how to modify or extend its configuration.

Below is a breakdown of each major directory in [https://github.com/destination-earth/DestinE-DataLake-Gallery.git](https://github.com/destination-earth/DestinE-DataLake-Gallery.git) and its purpose, followed by a step by step tutorial on how to contribute:

---

# Files and Folder Structure

## 1. _static/

The `custom.css` file defines the visual appearance of the site, including colors, font styles, spacing, and header size.

To make design changes (e.g., colors, fonts), you can directly edit `custom.css`. These changes will be automatically applied with every push, without additional steps required.

---

## 2. img/

This folder contains all images used by the notebooks or the website itself. When adding a new notebook, you can include a thumbnail image and reference it in the first Markdown cell.

Please have a look at the the Contributing section below!

---

## 3. scripts/

Each step in the workflow is handled by a dedicated Python script that automates the gallery generation and site configuration process. The scripts are:

### `clone_sync_repos.py`

Clones the current version of the repository
[https://github.com/destination-earth/DestinE-DataLake-Lab.git](https://github.com/destination-earth/DestinE-DataLake-Lab.git) (branch: `staging`) and copies the three subfolders `HDA`, `HOOK`, and `STACK` into the local `production/` directory. It also reads the `cookbooks.json` file and clones each listed repository (optionally with a branch and subfolder). All valid entries are copied into `production/` and their images into `img/`.

### `generate_gallery_md.py`

Generates a gallery page for each subfolder within `production/`.
It extracts metadata (title, description, tags) from the first Markdown cell of each notebook and creates a gallery card using HTML `<div>` blocks.

Generated gallery pages are stored in the `galleries/` folder.

> **Note:** To adjust the card design, edit the corresponding HTML layout directly in this script.

### `generate_keywords.py`

Creates tag‑specific gallery pages by scanning the first Markdown cell of each notebook, extracting the tags, and generating one gallery per tag.
The resulting pages are stored in the `galleries_by_tag/` folder.

### `parse_issue.py`

Parses the content of the issue template and generates a `cookbook.json` file.
This script is automatically triggered whenever a new cookbook is submitted to be added to the website.

### `indexbutton.py`

Automatically updates `index.md` and all gallery markdown files by inserting or replacing a section of tag filter buttons.
It scans the `galleries_by_tag/` folder and generates corresponding `{button}` links.

The script locates the marker `### Filter Notebooks by Tags` in each file and replaces the section below it with the updated tag buttons — keeping all gallery pages synchronized with new tags automatically.

### `build_myst_yml.py`

Automatically generates the `myst.yml` configuration file.
This script includes references to `index.md`, `contribute.md`, `footer.md` and all files within the `production/` folder.
It also defines global website configuration such as theme, style, logo and hidden elements.

> **Note:** Any structural changes to the site (navigation, theme, or appearance) must be made in this script — not directly in `myst.yml`, since that file is dynamically generated here.

---

## 4. github/

This folder contains two key subfolders:

### ISSUE_TEMPLATE/

This folder contains the issue template used to submit new cookbooks.
See the Contributing section below for more details.

The file `submit_repo.yml` defines the structure of the submission form.

### workflows/

This folder contains the GitHub Actions workflows that power the automation. The two workflows are:

#### `build_myst_page.yml`

This workflow is automatically triggered on every push to the `main` branch.

It executes the following Python scripts:

* Clone external notebook repository → `clone_sync_repos.py`
* Generate gallery markdown files → `generate_gallery_md.py`
* Generate tag-based gallery pages → `generate_keywords.py`
* Insert tag filter buttons in all pages → `indexbutton.py`
* Generate myst.yml and Table of Contents → `build_myst_yml.py`

After execution, it updates and commits:

* `production/`
* `galleries/`
* `galleries_by_tag/`
* `img/`
* `myst.yml`
* `index.md`

#### `integrate_cookbook.yml`

This workflow is triggered only when an issue is closed, and only if the actor is `katharinastarzer21` or `koenifra`.

> **Note:** This restriction should be adjusted based on team access permissions in the future.

Once triggered, the workflow performs these steps:

* Dump issue content to a file → `issue_body.txt`
* Parse the submitted issue template → `parse_issue.py`
* Clone external cookbooks into production → `clone_sync_repos.py`
* Generate gallery markdown pages → `generate_gallery_md.py`
* Generate tag-based gallery pages → `generate_keywords.py`
* Insert tag filter buttons → `indexbutton.py`
* Build the myst.yml configuration → `build_myst_yml.py`

This ensures the submitted content (like a new `HDA`, `HOOK`, or `STACK` repository) is added via `cookbook.json`.
It will then be included automatically in future builds.

---

## 5. Additional Files

### `myst.yml`

This file defines the structure and configuration of the MyST site.
It is automatically generated and updated by the script `build_myst_yml.py`.

### `footer.md`

Contains the footer content that appears on every page of the gallery.
You can easily modify or extend it if you want to update contact details or design elements.

### `contribute.md`

Provides contribution guidelines similar to the “How to Contribute” section in this documentation.
You can update it to reflect new submission rules or workflow instructions.

### `cookbooks.json`

Stores metadata about all externally added cookbooks.
Currently, it is empty but gets automatically updated by the `integrate_cookbook.yml` workflow through the script `clone_sync_repos.py`.
It ensures that any new repositories submitted via issues are included in future builds.

---

# How to Contribute

First, decide whether you want to:

* Add a notebook to an existing section (HDA, HOOK or STACK) or
* Add a completely new section to the website.

## Adding a notebook to an existing section

If your notebook fits into one of the existing sections, make sure to:

1. **Use the official notebook template:**
   [https://github.com/destination-earth/DestinE-DataLake-NotebookTemplate/blob/main/notebooks/template.ipynb](https://github.com/destination-earth/DestinE-DataLake-NotebookTemplate/blob/main/notebooks/template.ipynb)

2. **Push your notebook to the staging branch:**

If you use a new thumbnail or an additional image: Please make sure to include your images in the img/ folder in the following repo and add your notebook to the corresponding folder.
[https://github.com/destination-earth/DestinE-DataLake-Lab/tree/staging](https://github.com/destination-earth/DestinE-DataLake-Lab/tree/staging)

> **Note:** Until the workflow is changed to track the main branch, notebooks must be added to the staging branch. The script clone_sync_repos.py uses this branch.

After the next execution of build_myst_page.yml, your notebook will appear on the website.

> **Tip:** You can manually trigger this workflow:
> Go to [https://github.com/destination-earth/DestinE-DataLake-Gallery/actions/workflows/build_myst_page.yml](https://github.com/destination-earth/DestinE-DataLake-Gallery/actions/workflows/build_myst_page.yml) and click **Run workflow**.

## Adding a new section to the gallery

If you’ve developed a new notebook repository that works with DestinE Data Lake services and want to add it as a new section:

### Step-by-Step Instructions

1. **Use the Template Repository**

   * Clone the template repository:
     `git clone https://github.com/destination-earth/DestinE-DataLake-NotebookTemplate.git`
   * Or use the **"Use this template"** button on GitHub to start your own repository.

2. **Add Your Content**

   * Place your notebooks in the notebooks/ folder.
   * Use the format of template.ipynb. Be sure the first cell is YAML metadata!
   * Store any images in the img/ folder and reference

## Adding a new section to the gallery

If you’ve developed a new notebook repository that works with DestinE Data Lake services and want to add it as a new section:

### Step-by-Step Instructions

1. **Use the Template Repository**

   * Clone the template repository:
     `git clone <https://github.com/destination-earth/DestinE-DataLake-NotebookTemplate.git>`
   * Or use the **"Use this template"** button on GitHub to start your own repository.

2. **Add Your Content**

   * Place your notebooks in the notebooks/ folder.
   * Use the format of template.ipynb. Be sure the first cell is YAML metadata!
   * Store any images in the img/ folder and reference them correctly.

3. **Configure Repository Settings**

   * Enable GitHub Pages: Settings → Pages → Source: GitHub Actions
   * Enable Workflow Permissions: Settings → Actions → General → Workflow permissions → Read and write permissions

4. **Submit Your Repository**

   * Open an issue using this link:
     [https://github.com/destination-earth/DestinE-DataLake-Gallery/issues](https://github.com/destination-earth/DestinE-DataLake-Gallery/issues)
   * Provide the following info:

     * Title of the submission
     * Repository URL
     * Short uppercase title for folder naming

5. **Review and Integration**

   * The team will review your submission and when the issue is closed, it will be automatically integrated into the gallery.

### Best Practices

* Use clear, descriptive titles and consistent structure.
* Choose meaningful, well-formatted tags (e.g., no typos or inconsistent casing).
* Keep notebooks minimal and well-documented.
* Ensure the notebook runs from top to bottom without errors.
* Add helpful explanations and context for users.

# Contribute to the Gallery

If you’ve developed a Jupyter notebook that works with the **DestinE Data Lake** services and would like to share it with others, follow the steps below to add your repository to the Gallery:

## Step-by-Step: Add an External Cookbook Repository

### 1. Use the official notebook template

Start from the official template repository:

```bash
git clone https://github.com/destination-earth/DestinE-DataLake-NotebookTemplate.git
```

Alternatively, click **“Use this template”** on GitHub to create your own repository.

Your repository **must** contain the following structure:

```
notebooks/
img/
```


### 2. Add your notebooks and images

* Place all Jupyter notebooks in the `notebooks/` folder.
* Each notebook **must** follow the structure of `notebooks/template.ipynb`.
* The **first Markdown cell** of every notebook must contain valid YAML front matter, for example:

```markdown
---
title: "Your Notebook Title"
subtitle: "Brief description of what this notebook does."
authors: ["Your Name"]
tags: ["Climate", "Hydrology"]
thumbnail: img/example.png
license: MIT
---
```

* Store all images (including thumbnails) in the `img/` folder.
* Reference images using relative paths (e.g. `img/example.png`).

### 3. Prepare your repository branches

You can decide **which branch** of your repository should be used for:

* the **staging gallery preview**
* the **main (production) gallery**

Common setups are:

* `staging` → preview
* `main` → production

### 4. **Configure repository settings**

   * **Enable GitHub Pages**

     * Go to **Settings → Pages**.
     * Under Build and deployment, set Source to GitHub Actions.

   * **Enable Required GitHub Actions Permissions**

     * Go to **Settings → Actions → General**.
     * Scroll to **Workflow permissions**.
     * Select **Read and write permissions**.
     * Click **Save** if you made any changes.


### 5. Submit your repository via the Gallery issue form

Open the **“Add new cookbook”** issue form in the Gallery repository:

[https://github.com/destination-earth/DestinE-DataLake-Gallery/issues](https://github.com/destination-earth/DestinE-DataLake-Gallery/issues)

Provide the following information:

* Submission title
* Repository URL (HTTPS)
* Short folder name in **UPPERCASE** (used in the gallery structure)
* Branch for the **staging gallery**
* Branch for the **main gallery**

Once submitted, the issue will automatically receive the label **`add-repo`**.

### 6. Automatic staging preview

After submission:

* your repository is automatically added to the **staging gallery**
* notebooks are validated (metadata, structure)
* the staging gallery is rebuilt

This allows maintainers to review:

* layout
* metadata
* tags
* images
* overall quality

### 7. Review and promotion

* If the submission is approved, a maintainer adds the label **`promote-to-main`**.
* This triggers an automated workflow that updates the **main gallery**.
* If issues are found, maintainers may instead apply **`remove-repo`**, which removes the cookbook from staging.

> External cookbooks **always enter STAGING first**.
> Nothing appears in the public gallery without explicit promotion.

## Best Practices

* Use clear, descriptive titles and subtitles.
* Reuse existing tags where possible to keep the gallery consistent.
* Ensure correct spelling and consistent casing of tags.
* Keep dependencies minimal and well documented.
* Make sure notebooks run top-to-bottom without errors.
* Add explanations so users understand the workflow and purpose.

## Important Note

Once your cookbook is accepted into the **main gallery**,
**any future changes you push to the selected branch** of your repository will automatically appear on the website during the next gallery build.

Please keep your repository clean, stable, and well maintained.

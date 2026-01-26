# Contribute to the Gallery

If you’ve developed a Jupyter notebook that works with the **DestinE Data Lake** services and would like to share it with others, follow the steps below to add your repository to the Gallery:

### Step-by-Step: Upload Your Repository

1. **Use the template repository**

   * Clone the official template repository to your own GitHub account:

     ```bash
     git clone https://github.com/destination-earth/DestinE-DataLake-NotebookTemplate.git
     ```
   * Or click the **"Use this template"** button on GitHub to create your own copy.

2. **Add your content**

   * Place your Jupyter Notebooks in the `notebooks/` folder.
   * Follow the example in `notebooks/template.ipynb`, paying close attention to the **first Markdown cell**, which must contain a YAML front matter block:

     ```markdown
     ---
     title: "Your Notebook Title"
     subtitle: "Brief description of what this notebook does."
     authors: ["Your Name"]
     tags: ["Template"]
     thumbnail: /img/example.png
     license: MIT
     copyright: "© 2024 EUMETSAT"
     ---
     ```
   * Add a thumbnail image for each notebook, store it in the `img/` folder, and reference it in the notebook metadata.

3. **Configure repository settings**

   * **Enable GitHub Pages**

     * Go to **Settings → Pages**.
     * Under Build and deployment, set Source to GitHub Actions.

   * **Enable Required GitHub Actions Permissions**

     * Go to **Settings → Actions → General**.
     * Scroll to **Workflow permissions**.
     * Select **Read and write permissions**.
     * Click **Save** if you made any changes.

4. **Submit your repository**

   * Open the [Gallery submission issue form](https://github.com/destination-earth/DestinE-DataLake-Lab/issues/new/choose). And choose issue named:Ad new cookbook.
   * Provide:

     * Title (e.g. action)
     * Repository URL
     * Short title in **UPPERCASE** (for folder naming)

5. **Review process**

   * The DestinE team will review your submission.
   * If accepted, it will be integrated into the official gallery and published automatically.

### Best Practices

* Use clear titles and logical section headings.
* Tag your notebooks meaningfully. Whenever possible, review the tags already used in the gallery and reuse them to maintain consistency. Pay close attention to correct spelling and case sensitivity (e.g., uppercase/lowercase).
* Keep dependencies minimal and list them explicitly.
* Ensure your notebook runs from top to bottom without errors.
* Add explanations and context so users understand the workflow.

### Attention!

Once accepted, **any changes** you push to your repository will **automatically** appear on the website. Keep your repository clean, well-maintained, and up to date.


Good catch — your current **Contribute** text is *close*, but a few parts are **no longer true** given how your system actually works now (staging → promote-to-main, branches per cookbook, no GitHub Pages in external repos, etc.).

Below is a **corrected and aligned version**, keeping your structure but fixing the factual issues.

---

# Contribute to the DEDL Notebook Gallery

If you have developed a Jupyter notebook that works with **Destination Earth Data Lake services** and would like to share it with others, you can contribute it to the **DEDL Notebook Gallery** by following the steps below.

There are two ways to contribute:

* add a notebook to an existing service section (HDA, HOOK, STACK), or
* propose a **new notebook collection** via an external repository (“cookbook”).

This section describes how to contribute an **external cookbook repository**.

---

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

---

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

---

### 3. Prepare your repository branches

You can decide **which branch** of your repository should be used for:

* the **staging gallery preview**
* the **main (production) gallery**

Common setups are:

* `staging` → preview
* `main` → production

You will specify both branches during submission.

> You **do not** need to enable GitHub Pages in your repository.
> The gallery is built centrally — your repository is only cloned and read.

---

### 4. Submit your repository via the Gallery issue form

Open the **“Add new cookbook”** issue form in the Gallery repository:

[https://github.com/destination-earth/DestinE-DataLake-Gallery/issues](https://github.com/destination-earth/DestinE-DataLake-Gallery/issues)

Provide the following information:

* Submission title
* Repository URL (HTTPS)
* Short folder name in **UPPERCASE** (used in the gallery structure)
* Branch for the **staging gallery**
* Branch for the **main gallery**

Once submitted, the issue will automatically receive the label **`add-repo`**.

### 5. Automatic staging preview

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


### 6. Review and promotion

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

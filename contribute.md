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

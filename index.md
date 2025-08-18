# DestinE Data Lake Gallery

**Welcome to the Destination Earth Data Lake Notebook Gallery!** <br>
Explore our collection of interactive Jupyter Notebooks, designed to help you work with the wide range of services offered by the DestinE Data Lake. Each notebook provides hands-on examples and practical guidance that you can adapt for your own projects. <br>
Use the tag filters to quickly find notebooks relevant to your interests or workflow. Tags group notebooks by topic, data source, or functionality, making it easier to navigate the gallery and locate the examples most useful for your work.

---

### Filter Notebooks by Tags


{button}`Access Token <galleries_by_tag/tag-access-token.md>`
{button}`Authentication <galleries_by_tag/tag-authentication.md>`
{button}`Avhrr <galleries_by_tag/tag-avhrr.md>`
{button}`C3S <galleries_by_tag/tag-c3s.md>`
{button}`Cluster <galleries_by_tag/tag-cluster.md>`
{button}`Core Api <galleries_by_tag/tag-core-api.md>`
{button}`Dask <galleries_by_tag/tag-dask.md>`
{button}`Datacube <galleries_by_tag/tag-datacube.md>`
{button}`Digital Twin <galleries_by_tag/tag-digital-twin.md>`
{button}`Earthkit <galleries_by_tag/tag-earthkit.md>`
{button}`Ecmwf <galleries_by_tag/tag-ecmwf.md>`
{button}`Eodag <galleries_by_tag/tag-eodag.md>`
{button}`Gfm <galleries_by_tag/tag-gfm.md>`
{button}`Hda <galleries_by_tag/tag-hda.md>`
{button}`Hook <galleries_by_tag/tag-hook.md>`
{button}`Http Requests <galleries_by_tag/tag-http-requests.md>`
{button}`Metop <galleries_by_tag/tag-metop.md>`
{button}`Olci <galleries_by_tag/tag-olci.md>`
{button}`Pyaviso <galleries_by_tag/tag-pyaviso.md>`
{button}`Satpy <galleries_by_tag/tag-satpy.md>`
{button}`Sentinel 3 <galleries_by_tag/tag-sentinel-3.md>`
{button}`Seviri <galleries_by_tag/tag-seviri.md>`
{button}`Stac <galleries_by_tag/tag-stac.md>`
{button}`Stack <galleries_by_tag/tag-stack.md>`
{button}`Storage <galleries_by_tag/tag-storage.md>`
{button}`Token <galleries_by_tag/tag-token.md>`
{button}`Workflow <galleries_by_tag/tag-workflow.md>`

---

### Services Overview

The DestinE Data Lake provides three main services to help you discover, process, and manage data:

* **[Harmonised Data Access (HDA)](https://hda.data.destination-earth.eu/stac)** – Browse Jupyter Notebook examples and Python tools for the DEDL Harmonised Data Access.
* **[STACK service](https://s3.central.data.destination-earth.eu/swift/v1/dedl_datacube)** – Leverage Dask for scalable, near-data processing of large datasets.
* **[HOOK service](https://odp.data.destination-earth.eu/odata/v1/)** – Create, manage, and automate workflows using the HOOK orchestration service.

---

### Using Notebooks on the DestinE Platform

If you are working in the DestinE JupyterLab environment, set up your environment as follows:

```bash
# 1. Create a virtual environment
python -m venv /home/jovyan/my_env

# 2. Activate the environment
source /home/jovyan/my_env/bin/activate

# 3. Install required dependencies
pip install -r /home/jovyan/datalake-lab/requirements.txt

# 4. Register the environment as a Jupyter kernel
python -m ipykernel install --name my_env --user
```

After installation, choose `my_env` from the Jupyter kernel menu to start running notebooks.

---

## Want to Contribute?

Have a useful notebook to share? Check out our [Contributing Guide](contribute.md) to learn how to add it to the gallery.

---

## Learn More

* [DestinE Documentation](https://destine-data-lake-docs.data.destination-earth.eu/en/latest/index.html) – Full platform and service documentation.
* [DestinE Data Portfolio](https://hda.data.destination-earth.eu/ui/catalog) – Browse available datasets.
* [API Documentation (Swagger)](https://hda.data.destination-earth.eu/docs/) – Explore the API endpoints and capabilities.

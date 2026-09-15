# DestinE Data Lake Gallery

**Welcome to the Destination Earth Data Lake Notebook Gallery!** <br>
Explore our collection of interactive Jupyter Notebooks, designed to help you work with the wide range of services offered by the DestinE Data Lake. Each notebook provides hands-on examples and practical guidance that you can adapt for your own projects. <br>
Use the tag filters to quickly find notebooks relevant to your interests or workflow. Tags group notebooks by topic, data source, or functionality, making it easier to navigate the gallery and locate the examples most useful for your work.

---

### Filter Notebooks by Tags









{button}`Access Token <galleries_by_tag/tag-access-token.md>`
{button}`Authentication <galleries_by_tag/tag-authentication.md>`
{button}`AVHRR <galleries_by_tag/tag-avhrr.md>`
{button}`C3S <galleries_by_tag/tag-c3s.md>`
{button}`Cluster <galleries_by_tag/tag-cluster.md>`
{button}`Core API <galleries_by_tag/tag-core-api.md>`
{button}`Dask <galleries_by_tag/tag-dask.md>`
{button}`Digital Twin <galleries_by_tag/tag-digital-twin.md>`
{button}`earthkit <galleries_by_tag/tag-earthkit.md>`
{button}`ECMWF <galleries_by_tag/tag-ecmwf.md>`
{button}`EODAG <galleries_by_tag/tag-eodag.md>`
{button}`GFM <galleries_by_tag/tag-gfm.md>`
{button}`HDA <galleries_by_tag/tag-hda.md>`
{button}`Hook <galleries_by_tag/tag-hook.md>`
{button}`HTTP requests <galleries_by_tag/tag-http-requests.md>`
{button}`Metop <galleries_by_tag/tag-metop.md>`
{button}`OLCI <galleries_by_tag/tag-olci.md>`
{button}`pyaviso <galleries_by_tag/tag-pyaviso.md>`
{button}`satpy <galleries_by_tag/tag-satpy.md>`
{button}`Sentinel-3 <galleries_by_tag/tag-sentinel-3.md>`
{button}`SEVIRI <galleries_by_tag/tag-seviri.md>`
{button}`STAC <galleries_by_tag/tag-stac.md>`
{button}`STACK <galleries_by_tag/tag-stack.md>`
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

## Notebooks Execution Environment

Notebooks in this gallery are designed to run in the [**DEDL STACK**](https://jupyter.central.data.destination-earth.eu/hub/) environment using the default **Python DEDL** kernel.

For users planning to run these notebooks outside the DEDL Stack environment, the file [`dedl-python-kernel-packages.txt`](https://raw.githubusercontent.com/destination-earth/DestinE-DataLake-Lab/refs/heads/main/dedl-python-kernel-packages.txt) provides the list of libraries currently available in the default **Python DEDL** kernel and can be used as a reference when setting up a local environment (dedl-python-kernel-packages.txt file obtained via the *pip list --format=freeze > dedl-python-kernel-packages.txt* command in the DEDL STACK).


### Availability in Insula

A subset of these notebooks is also available to Insula users through the Insula Code environment:

https://code.insula.destine.eu/hub/

When running the notebooks in Insula, please follow the environment-specific instructions provided below. 

#### DestinE Platform Insula Service Users
<br>
Please perform the following and select my-datalake-lab kernel when running the provided Notebooks<br>

Open a terminal window (File -> New -> Terminal) and run the following commands in sequence:

Create a virtual environment: 
     
     python -m venv /home/jovyan/my-datalake-lab

Activate it: 
     
     source /home/jovyan/my_datalake_lab/bin/activate

Install required dependencies for this example Notebooks:

     pip install -r /home/jovyan/datalake-lab-insula/HDA/insula-requirements.txt

Verify the installation:
     
     pip list | grep destinelab

This should give:

destinelab         1.14

Install kernel my_env. Run the command:

     python -m ipykernel install --name my_datalake_lab --user

**Select the kernel my_datalake_lab from the top-right menu of these notebooks.**

Users who already have a previous version of the 'my_datalake_lab' environment installed, should delete the kernel before running the steps above. 

To delete the my_datalake_lab kernel please run the following command: 'jupyter kernelspec uninstall my_datalake_lab' from a terminal window.

---

## Want to Contribute?

Have a useful notebook to share? Check out our [Contributing Guide](contribute.md) to learn how to add it to the gallery.

---

## Learn More

* [DestinE Documentation](https://destine-data-lake-docs.data.destination-earth.eu/en/latest/index.html) – Full platform and service documentation.
* [DestinE Data Portfolio](https://hda.data.destination-earth.eu/ui/catalog) – Browse available datasets.
* [API Documentation (Swagger)](https://hda.data.destination-earth.eu/docs/) – Explore the API endpoints and capabilities.

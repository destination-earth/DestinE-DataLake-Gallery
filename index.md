# DEDL Notebook Gallery

<!--
```{card} Card title
:header: The _Header_
:footer: Footer
Card content

![EUMETSAT Logo](img/EUMETSAT-logo.png)
hallo
```
-->

<img style="float:left; width:5%" src="./img/EUMETSAT-icon.png"/>  
<br>

# DestinE Data Lake Notebook Gallery

<img style="float:left; width:5%; margin-right: 10px;" src="./img/EUMETSAT-icon.png"/>

Welcome to the **Destination Earth Data Lake Laboratory** – your interactive environment for exploring and working with DestinE Data Lake services.  
This gallery provides practical Jupyter Notebook examples and tools for accessing, processing, and analyzing Earth observation data using the three core services:

---

### Harmonised Data Access (HDA)

Easily query and download datasets from the DestinE Data Lake using the **HDA API**.

- 🔹 Access EO data via standardised APIs  
- 🔹 Explore Python examples for automated querying and downloading  
- 🔗 [HDA Notebook Gallery](galleries/HDA.md)  
- 🔗 [HDA GitHub Repository](https://github.com/destination-earth/DestinE-DataLake-Lab/tree/main/HDA)

---

### STACK – Scalable Data Processing

Run heavy data analytics **close to the data** using Dask-powered processing within the Data Lake infrastructure.

- 🔹 Learn how to use Dask for efficient, distributed computations  
- 🔹 Example notebooks for setting up, scaling, and executing workflows  
- 🔗 [STACK Notebook Gallery](galleries/STACK.md)  
- 🔗 [STACK GitHub Repository](https://github.com/destination-earth/DestinE-DataLake-Lab/tree/main/STACK)

---

### HOOK – Workflow Automation

Design and execute reproducible **EO processing workflows** using the HOOK orchestration system.

- 🔹 Discover how to use HOOK for workflow management and automation  
- 🔹 Create, manage, and monitor processing chains  
- 🔗 [HOOK Notebook Gallery](galleries/HOOK.md)  
- 🔗 [HOOK GitHub Repository](https://github.com/destination-earth/DestinE-DataLake-Lab/tree/main/HOOK)

---

## Documentation & Resources

> Find more information and technical documentation in the official DestinE Data Lake Docs:  
👉 [DestinE Docs](https://destine-data-lake-docs.data.destination-earth.eu/en/latest/index.html)

### 🔗 Useful Links

- **DestinE Data Portfolio**  
  [https://hda.data.destination-earth.eu/ui/catalog](https://hda.data.destination-earth.eu/ui/catalog)

- **Priority Services Overview**  
  [https://hda.data.destination-earth.eu/ui/services](https://hda.data.destination-earth.eu/ui/services)

- **HDA Swagger UI**  
  [https://hda.data.destination-earth.eu/docs/](https://hda.data.destination-earth.eu/docs/)

  ## 🧭 Getting Started on the DestinE Platform (Insula)

To get started on the **DestinE Insula Jupyter environment**, follow these steps and use the kernel `my_env` in all notebooks:

### 1. Open a terminal window (File → New → Terminal) and run:

```bash
# Create a new virtual environment
python -m venv /home/jovyan/my_env

# Activate it
source /home/jovyan/my_env/bin/activate

# Install all required Python dependencies
pip install -r /home/jovyan/datalake-lab/requirements.txt

# Optional: Verify the destinelab package is installed
pip list | grep destinelab
# → Should return: destinelab 0.9


## Notebook Filter


{button}`Stack <galleries/STACK.md>`
{button}`HDA <galleries/HDA.md>`
{button}`HOOK <galleries/HOOK.md>`
{button}`Access Token <galleries_by_tag/tag-access-token.md>`
{button}`Authentication <galleries_by_tag/tag-authentication.md>`
{button}`Authentification <galleries_by_tag/tag-authentification.md>`
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
{button}`Sentinel 1 <galleries_by_tag/tag-sentinel-1.md>`
{button}`Sentinel 2 <galleries_by_tag/tag-sentinel-2.md>`
{button}`Sentinel 3 <galleries_by_tag/tag-sentinel-3.md>`
{button}`Seviri <galleries_by_tag/tag-seviri.md>`
{button}`Stac <galleries_by_tag/tag-stac.md>`
{button}`Stack <galleries_by_tag/tag-stack.md>`
{button}`Storage <galleries_by_tag/tag-storage.md>`
{button}`Thresholding Techniques <galleries_by_tag/tag-thresholding-techniques.md>`
{button}`Token <galleries_by_tag/tag-token.md>`
{button}`Workflow <galleries_by_tag/tag-workflow.md>`

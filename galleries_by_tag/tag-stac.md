# Notebooks `STAC`

### Filter Notebooks by Tags

{button}`Access Token <./tag-access-token.md>`
{button}`Authentication <./tag-authentication.md>`
{button}`Avhrr <./tag-avhrr.md>`
{button}`C3S <./tag-c3s.md>`
{button}`Cluster <./tag-cluster.md>`
{button}`Core Api <./tag-core-api.md>`
{button}`Dask <./tag-dask.md>`
{button}`Datacube <./tag-datacube.md>`
{button}`Digital Twin <./tag-digital-twin.md>`
{button}`Earthkit <./tag-earthkit.md>`
{button}`Ecmwf <./tag-ecmwf.md>`
{button}`Eodag <./tag-eodag.md>`
{button}`Gfm <./tag-gfm.md>`
{button}`Hda <./tag-hda.md>`
{button}`Hook <./tag-hook.md>`
{button}`Http Requests <./tag-http-requests.md>`
{button}`Metop <./tag-metop.md>`
{button}`Olci <./tag-olci.md>`
{button}`Pyaviso <./tag-pyaviso.md>`
{button}`Satpy <./tag-satpy.md>`
{button}`Sentinel 3 <./tag-sentinel-3.md>`
{button}`Seviri <./tag-seviri.md>`
{button}`Stac <./tag-stac.md>`
{button}`Stack <./tag-stack.md>`
{button}`Storage <./tag-storage.md>`
{button}`Token <./tag-token.md>`
{button}`Workflow <./tag-workflow.md>`

<div style="display: flex; flex-direction: column; gap: 20px; max-width: 800px;">
<div class="notebook-card" data-tags="HDA STAC ECMWF" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
  <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
    <img src="../img/EUMETSAT-icon.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
  </div>
  <div style="flex: 1;">
    <strong>ERA5 hourly data on single levels from 1940 to present</strong><br>
    This notebook shows how to authenticate with the DestinE API, queries and downloads ERA5 single-level reanalysis data using the DEDL HDA service, and visualizes the result with EarthKit.
    <div style="margin: 6px 0;">
      <span class="tag">HDA</span><span class="tag">STAC</span><span class="tag">ECMWF</span>
    </div>
    <a href="../production/HDA/CDS_data/DEDL-HDA-EO.ECMWF.DAT.REANALYSIS_ERA5_SINGLE_LEVELS.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
  </div>
</div>
<div class="notebook-card" data-tags="HDA STAC Core API" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
  <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
    <img src="../img/hda.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
  </div>
  <div style="flex: 1;">
    <strong>HDA Tutorial</strong><br>
    This notebook demonstrates the first steps using the Harmonised Data access API.
    <div style="margin: 6px 0;">
      <span class="tag">HDA</span><span class="tag">STAC</span><span class="tag">Core API</span>
    </div>
    <a href="../production/HDA/REST/HDA-REST-full-version.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
  </div>
</div>
<div class="notebook-card" data-tags="HDA STAC HTTP requests" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
  <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
    <img src="../img/hda.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
  </div>
  <div style="flex: 1;">
    <strong>HDA Tutorial - Quick start</strong><br>
    This notebook demonstrates how to use the HDA (Harmonized Data Access) API by sending a few HTTP requests to the API, using Python code.
    <div style="margin: 6px 0;">
      <span class="tag">HDA</span><span class="tag">STAC</span><span class="tag">HTTP requests</span>
    </div>
    <a href="../production/HDA/REST/HDA-REST-quick-start.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
  </div>
</div>
<div class="notebook-card" data-tags="STAC Authentication Access Token" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
  <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
    <img src="../img/hda.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
  </div>
  <div style="flex: 1;">
    <strong>Using HDA to Find and Download Data for Urban Area Monitoring Using Sentinel-1 Data</strong><br>
    In this notebook, we will present a simple example of how you can access data from DEDL using HDA and what you can do with it. We will demonstrate how to utilize thresholding techniques and compare the values of VV and VH polarizations to analyze urban areas. As an illustration, we will attempt to download Sentinel-1 images containing data of the urban area of Warsaw (Poland).
    <div style="margin: 6px 0;">
      <span class="tag">STAC</span><span class="tag">Authentication</span><span class="tag">Access Token</span>
    </div>
    <a href="../production/HDA/REST/DEDL-HDA-EO.ESA.DAT.SENTINEL-1.L1_GRD.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
  </div>
</div>
<div class="notebook-card" data-tags="STAC Authentication Access Token" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
  <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
    <img src="../img/hda.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
  </div>
  <div style="flex: 1;">
    <strong>How to use HDA to find and download data for conducting monitoring of Śniadrwy lake</strong><br>
    In this notebook, we will present a simple example on how you can access data from DEDL using HDA and what you can do with it. As an example, we will try to download Sentinel-2 images containining data of Śniadrwy lake from first week of July 2023. With usage of HDA and few Python packages, you will be able to obtain rasters with NDWI index.
    <div style="margin: 6px 0;">
      <span class="tag">STAC</span><span class="tag">Authentication</span><span class="tag">Access Token</span>
    </div>
    <a href="../production/HDA/REST/DEDL-HDA-EO.ESA.DAT.SENTINEL-2.MSI.L2A.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
  </div>
</div>
<div class="notebook-card" data-tags="STAC Authentication Access Token" style="display: flex; align-items: flex-start; border: 1px solid #cddff1; border-radius: 6px; padding: 14px 20px; background-color: #f9fbfe; box-shadow: 1px 1px 4px #dfeaf5;">
  <div style="width: 100px; height: 100px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; background-color: #fff; border: 1px solid #e0eaf5; border-radius: 6px; overflow: hidden; margin-right: 32px;">
    <img src="../img/STAC-01.png" alt="Notebook Thumbnail" style="max-width: 100%; max-height: 100%; object-fit: contain;">
  </div>
  <div style="flex: 1;">
    <strong>HDA PySTAC-Client Introduction</strong><br>
    This notebook shows the basic use of DestinE Data Lake Harmonised Data Access using pystac-client.
    <div style="margin: 6px 0;">
      <span class="tag">STAC</span><span class="tag">Authentication</span><span class="tag">Access Token</span>
    </div>
    <a href="../production/HDA/PySTAC/HDA-PyStac-Client.ipynb" style="text-decoration: none; color: #1d70b8; font-weight: bold;">View Notebook</a>
  </div>
</div>
</div>

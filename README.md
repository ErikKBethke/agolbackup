# ArcGIS Online backup for python3

## Installation
Currently, the easiest way to install is from its ([source](https://github.com/ErikKBethke/tableau-workbook-xml)) on Github:

`pip install git+https://github.com/ErikKBethke/agolbackup`

## Disclaimer
This software is supplied "AS IS" without any warranties and support.

The author or Esri Sverige AB assumes no responsibility or liability for the use of the software, conveys no license or title under any patent, copyright, or mask work right to the product.

The author reserves the right to make changes in the software without notification. The author also make no representation or warranty that such application will be suitable for the specified use without further testing or modification.

**Always make sure your backups contain the data and attachments that you expect before deleting any data from ArcGIS Online**

## Description
Backup script to backup items in ArcGIS Online

### What it does
1. Logs you in to AGOL
2. Searches for all items of type 'Feature Service' (limit: 500 - can be changed)
3. For each search result, runs the export method on the item
4. For each exported item, runs the download method on the exported item
5. Deletes the exported item

## Requirements
* [ArcGIS Python API](https://developers.arcgis.com/python/) (comes with ArcGIS Pro)

## Updates
* 12/12/2019: Added setup automation

## To-Do
* Add dynamic installation options for: download location, users, etc.

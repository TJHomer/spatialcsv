# spatialcsv


[![image](https://img.shields.io/pypi/v/spatialcsv.svg)](https://pypi.python.org/pypi/spatialcsv)
[![image](https://img.shields.io/conda/vn/conda-forge/spatialcsv.svg)](https://anaconda.org/conda-forge/spatialcsv)


**Easily add location points to a map from a csv**


-   Free software: GNU General Public License v3
-   Documentation: https://tjhomer.github.io/spatialcsv/
    

## Features


This package takes csv files and standardizes them for web mapping. It will automatically change coordidantes from degree,minute format to decimal.

If using streamlit, it will change the column headers to what streamlit uses, and remove any empty coordinate fields (which causes streamlit to error out). To view in streamlit, go to https://spatialcsv.streamlit.app/

If using leafmap, you can add the following arguments:

* tags = [ ] Will select what columns are included in the pin popup
* epsg = '####' Will reproject from given crs to lat/long coordinates

If you don't want to use a web map, but only want to convert all the coordinates, there is also a function updated_csv() that will export it back to an csv file.

A video tutorial can be found here: https://vimeo.com/824586413

## Credits

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [giswqs/pypackage](https://github.com/giswqs/pypackage) project template.

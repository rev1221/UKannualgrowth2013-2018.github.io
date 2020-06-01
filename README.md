# UKannualgrowth2013-2018.github.io
1) dashapp.py is the python file container the plotly dependencies, if you wish to access it ensure your have uploaded the dependencies 
   by using pip install plotly==4.8.1 on command prompt alongside pip install pandas.(No need to pip instal json as its already installed 
   with python) and pip install xlrd to read excel file.
2) The data folder contains all the original data "uk annual growth rate by region.xlsx" based on this link "https://www.ons.gov.uk/filters/b6b07da4-e629-4d80-b07a-492d2712ef9e/dimensions".
   You are free to filter the data based on the ONS dataset:"https://www.ons.gov.uk/datasets/regional-gdp-by-year/editions/time-series/versions/4"
3) The data folder contains geojson files where the original "uk_regions_map.geojson" where I adapted it to suit the excel file 
   by removing areas such as scotland and northern ireland from the original geojson file into "map.geojson".
4) Assets folder contains css files used to provide style to the dashapp.py.

   

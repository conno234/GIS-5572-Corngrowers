# GIS-5572-Corngrowers

A file project for GIS 5572 to create a web app that can produce growing degree days, evapotranspiration, and temperature for the state of Minnesota in order to assist the Minnesota Corngrowers Association.


### ET Folder
-ET.ipynb: A Python notebook intended to be run in ArcGIS Pro. When used in conjection with the temp_data.csv, it allows one to inteprolate evapotranspiration data for the state of Minnesota for any day in September, 2023 and save the output as point features in a PostGIS database.

-temp_data.csv: A CSV table meant to be loaded into the working folder of the same ArcPro porject as the ET notebook. Contains NWS COOP Data for the State of Minnesota for the month of September, 2023.

### GDD Folder
-GDD.ipynb: A Python notebook intended to be run in ArcGIS Pro. When used in conjection with the rounded_gdd_data.csv, it allows one to inteprolate growing degree dats data for the state of Minnesota for any day in September, 2023 and save the output as point features in a PostGIS database.

-rounded_gdd_data.csv: A CSV table meant to be loaded into the working folder of the same ArcPro porject as the gdd notebook. Contains temperature and derived growing degree days for weather stations in the State of Minnesota for the month of September, 2023.

### Soil Folder
-GDD.ipynb: A Python notebook intended to be run in ArcGIS Pro. When used in conjection with the soil_moisture.tif, it allows one to convert a TIF of soil moisture in the state of Minnesota into point features that are saved in a PostGIS database.

-soil_moisture.tif: A TIF denoting soil moisture across Minnesota fetched from SMAP.

### Google Cloud Run
-Dockerfile: Used to connect to Cloud Run.

-requirements.txt: Provides the needed packages and specs needed to host a flask app.

-main.py: Connects to the PostGIS database and reads all three datatypes into the Cloud Run Instance.

### Google Cloud Run URLs
These links are produced by a connected Google Cloud Run instance. When the PostGIS database is running, clicking on these will lead one to GeoJSONs for their respective data.

-https://gis-5572-corngrowers-4jtpc5ugva-uc.a.run.app/gdd

-https://gis-5572-corngrowers-4jtpc5ugva-uc.a.run.app/et

-https://gis-5572-corngrowers-4jtpc5ugva-uc.a.run.app/soil

### ArcMap Viewer
-https://umn.maps.arcgis.com/home/item.html?id=4db2ef7631a9485a9a7c1236c4fe1241

This link links to a web map viewer within ArcGIS Online that displays the three map layers. All three maps automatically update with any new data loaded into the PostGIS database.

### ArcGIS Online Web Application
-https://experience.arcgis.com/experience/ed3d37d354d44eae98db9011de4516f6/

This link links to a web app within ArcGIS Online that displays the three map layers and also users to search for a particular location, thus enabling them to observe the points for each map layer around said location. Layers can also be hidden to make viewing data easier.

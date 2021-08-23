import os, sys, arcpy

class Geocoder:
    """This class represents how addresses are received, geocoded, and placed within the proper polygon.
  Parameters:
    - Address
    -- Street Prefix
    -- Street Number
    -- Street Direction
    -- Street Name
    -- Street type
    -- Street suffix
    -- City
    -- State
    -- Zip

    eg: 1100 South Hamilton Ave, Chicago, Il 60609
    --- Prefix: none
    --- Number: 1100
    --- Direction: South
    --- Name: Hamilton
    --- Type: Avenue
    --- Suffix: None

    Methods:
        parse address - recieve (post?)
        geocode address
    """




locator_path = sys.path(r"C:\Users\Public\ArcGIS\ccjpdLocator\MyProject1\Address_Points_geojson.loc")
police_district_layer = r"C:\Users\Public\ArcGIS\ccjpdLocator\MyProject1\Police Districts Chicago.lyrx"

#this seems to work


#next version will take a file

def geocode(address, locator_path, min_score = 90):
    locator = arcpy.geocoding.Locator(locator_path)
    candidate = locator.geocode(address, False)
    return([sub['Shape'] for sub in candidate][0])


x = geocode(police_16d, locator_path)
print(x)



lyrFile = arcpy.mp.LayerFile(police_district_layer)
#
# for lyr in lyrFile.listLayers():
#     print(lyr.name)

#Shape file since the layer isn't working right
shapefiles = r"C:\Users\Public\ArcGIS\ccjpdLocator\MyProject1\shapefiles\geo_export_245fc99a-723b-4ad0-ab19-164d6ea290d2.shp"


#This code does thie following: da.searchcursor goes through the shapefile (located at shapefile) which
#'SHAPE@' knows is a polygon, and then goes row by row to see if the POINT data (points) is in the right field.
#it prints 22. Trying to get it to print the name of the polygon, and this is where I'm stuck

#next step is a function
field = 'dist_num'
with arcpy.da.SearchCursor(shapefiles, ['SHAPE@', 'OID@', field]) as cursor:
    for row in cursor:
        polygonGeom = row[0]
        if polygonGeom.contains(x):
            print('the police district is = '+ str(row[2]))
            break
        #need code to return if no district was found


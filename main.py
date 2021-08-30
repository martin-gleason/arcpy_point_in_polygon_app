import os, sys, arcpy

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
    get_district: string of address, return police district or NONE if none
    geocode_address: string address, return points
"""

class Geocoder:
    def __init__(self, address = '1100 South Hamilton Ave, Chicago, Il 60612'):
        self.locator_path = os.path.realpath(r"ArcGIS Files\Address_Points_geojson.loc")
        self.address = address

    def __str__(self):
        return(f"The default locator path is {self.locator_path} and the default address is {self.address}")

    def geocode_address(address, locator_path, min_score=90):
      locator = arcpy.geocoding.Locator(locator_path)
      print("this is the locator " + str(locator))
      candidate = locator.geocode(address, False)
      print(candidate)
      return ([sub['Shape'] for sub in candidate][0])



# this seems to work


# next version will take a file

def geocode_address(address, locator_path, min_score=90):
    locator = arcpy.geocoding.Locator(locator_path)
    print("this is the locator " + str(locator))
    candidate = locator.geocode(address, False)
    print(candidate)
    return ([sub['Shape'] for sub in candidate][0])

gc = Geocoder()

print(gc.__str__())

#x = geocode('624 w 43rd Place, Chicago, il 60609', geojson_locator)
#print(x)

lyrFile = arcpy.mp.LayerFile(police_district_layer)
#
# for lyr in lyrFile.listLayers():
#     print(lyr.name)

# Shape file since the layer isn't working right
shapefiles = r"C:\Users\Public\ArcGIS\ccjpdLocator\MyProject1\shapefiles\geo_export_245fc99a-723b-4ad0-ab19-164d6ea290d2.shp"

# This code does thie following: da.searchcursor goes through the shapefile (located at shapefile) which
# 'SHAPE@' knows is a polygon, and then goes row by row to see if the POINT data (points) is in the right field.
# it prints 22. Trying to get it to print the name of the polygon, and this is where I'm stuck

# next step is a function
field = 'dist_num'
with arcpy.da.SearchCursor(shapefiles, ['SHAPE@', 'OID@', field]) as cursor:
    for row in cursor:
        polygonGeom = row[0]
        if polygonGeom.contains(x):
            print('the police district is = ' + str(row[2]))
            break
        # need code to return if no district was found

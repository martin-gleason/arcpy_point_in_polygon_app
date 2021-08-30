import os
import sys
import arcpy

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
        self.shape_file = os.path.realpath(r"ArcGIS Files\shapefiles\geo_export_245fc99a-723b-4ad0-ab19-164d6ea290d2.shp")

    def __str__(self):
        return f"The default locator path is {self.locator_path} and the default address is {self.address}"

    def geocode_address(self, address, min_score=90):
        locator = arcpy.geocoding.Locator(self.locator_path)
        candidate = locator.geocode(address, False)
        return [sub['Shape'] for sub in candidate][0]

    def return_district(self, point, shape_file):
        field = 'dist_num'
        with arcpy.da.SearchCursor(shape_file, ['SHAPE@', 'OID@', field]) as cursor:
            for row in cursor:
                polygonGeom = row[0]
                if polygonGeom.contains(point):
                    print('the police district is = ' + str(row[2]))
                    break

    def geocode_to_district(self, address):
        locator = arcpy.geocoding.Locator(self.locator_path)
        candidate = locator.geocode(address, False)
        point = [sub['Shape'] for sub in candidate][0]
        field = 'dist_num'
        with arcpy.da.SearchCursor(self.shape_file, ['SHAPE@', 'OID@', field]) as cursor:
            for row in cursor:
                polygonGeom = row[0]
                if polygonGeom.contains(point):
                    print('the police district is = ' + str(row[2]))
                    break



import os
import sys
import arcpy

"""This class represents how addresses are received, geocoded, and placed within the proper polygon.
Possible parameters:
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

Instance Methods:
    get_district: string of address, return police district or NONE if none
    geocode_address: string address, return points
    get_shape_file: returns location to path of shape file
    set_shape_file: a function to add a shapefile for finding/adding locations
    return_district: takes an address point, returns numerical police district
    geocode_to_district: Takes an address, geocodes it, and then returns numerical police district
"""

class Geocoder:
    def __init__(self, address = '1100 South Hamilton Ave, Chicago, Il 60612'):
        self.locator_path = os.path.abspath(r"C:\Users\martin.gleason\arcpy_point_in_polygon_app\ArcGIS Files\Address_Points_geojson.loc")
        self.address = address
        #thinking about turning this into a dictionary so we can have different ones called by name
        self.shape_file = os.path.realpath(r'ArcGIS Files\shapefiles\geo_export_245fc99a-723b-4ad0-ab19-164d6ea290d2.shp')
        #self.shape_file = os.path.realpath(r'ArcGIS Files\probation_districts\probationDistricts.shp')

    def __str__(self):
        return f'The default locator path is {self.locator_path}' \
        f' and the default address is {self.address}.' \
        f' The default shapefile for assignment is {self.shape_file}.'

    # def set_shape_file(self, shapefile):
    #     self.__setattr___(self, 'shape_file', shapefile)
    #     return f'The shapefile is {self.shape_file}'

    def get_shape_file(self):
        return f'The shapefile is {self.shape_file}'

    def geocode_address(self, address, min_score=90):
        locator = arcpy.geocoding.Locator(self.locator_path)
        candidate = locator.geocode(address, False)
        if len(candidate) == 0:
            return None
        else:
            return [sub['Shape'] for sub in candidate][0]

    def return_district(self, point, verbose = False):
        district = ''
        if point == None:
            return f'Calcuated address does not appear to be in Cook county'
        else:
            field = 'dist_num'
            with arcpy.da.SearchCursor(self.shape_file, ['SHAPE@', 'OID@', field]) as cursor:
                for row in cursor:
                    polygonGeom = row[0]
                    if polygonGeom.contains(point):
                        district = row[2]
            while verbose:
                if len(district) >= 1:
                    return district
                elif len(district) < 1:
                    return 'This address appears to be in Cook County, but not in Chicago.'
            else:
                return district

    def geocode_to_district(self, address):
        point = self.geocode_address(address)
        return self.return_district(point)




import geocoder as gc
import os
import arcpy

gc = gc.Geocoder()
point = ''

shape_file = os.path.abspath(r"C:\Users\martin.gleason\arcpy_point_in_polygon_app\ArcGIS Files\shapefiles\Municipality.shp")

#shape_file = os.path.abspath(r"C:\Users\martin.gleason\arcpy_point_in_polygon_app\ArcGIS Files\shapefiles\beats_districts.shp")

fields = arcpy.ListFields(shape_file)

for f in fields:
    print([field.name for field in arcpy.ListFields(shape_file)])

for field in fields:
     print("{0} is a type of {1} with a length of {2}".format(field.name, field.type, field.length))

print(fields[6])


def return_district(point, verbose=False):
    district = ""
    if point == None:
        return f'Calcuated address does not appear to be in Cook county'
    else:

        with arcpy.da.SearchCursor(shape_file, ['SHAPE@', 'OID@']) as cursor:
            for row in cursor:
                polygonGeom = row[0]
                if polygonGeom.contains(point):
                    district = "yes"
                else:
                    district = 'no'
        while verbose:
            if len(district) >= 1:
                return district
            elif len(district) < 1:
                return 'This address appears to be in Cook County, but not in Chicago.'
        else:
            return district



address = input('Please enter an address: ')
point = gc.geocode_address(address)

print(point)


x = return_district(point)

print(x)
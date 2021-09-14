#new geocoder with new shapefile
import os
import geocoder
import arcpy
gc = geocoder.Geocoder()

# def return_district(self, point, verbose = False):
#     district = ''
#     if point == None:
#         return f'Calcuated address does not appear to be in Cook county'
#     else:
#         field = 'dist_num'
#         with arcpy.da.SearchCursor(self.shape_file, ['SHAPE@', 'OID@', field]) as cursor:
#             for row in cursor:
#                 polygonGeom = row[0]
#                 if polygonGeom.contains(point):
#                     district = row[2]
#         while verbose:
#             if len(district) >= 1:
#                 return district
#             elif len(district) < 1:
#                 return 'This address appears to be in Cook County, but not in Chicago.'
#         else:
#             return district

a = '624 w 43rd Place, chicago, il 60609'
h = '736 terry lane, countryside, il 60525'
b = '10220 S 76th Ave #205l, Bridgeview, IL 60455'

a_point = gc.geocode_address(a)

print(gc.return_district(a_point))
shapefile = os.path.realpath(r'ArcGIS Files\shapefiles\geo_export_245fc99a-723b-4ad0-ab19-164d6ea290d2.shp')
shapefile = os.path.realpath(r'ArcGIS Files\probation_districts\probationDistricts.shp')

with arcpy.da.SearchCursor(shapefile, ['SHAPE@', 'OID', 'dist_num', 'MUNICIPALI']) as cursor:
    for row in cursor:
        polygonGeom=row[0]
        if polgonGeom.contains(a_point):
            print(row[2], row[3])
        



fields = arcpy.ListFields(shapefile)

for f in fields:
    print([field.name for field in arcpy.ListFields(shapefile)])

for field in fields:
    print("{0} is a type of {1} with a length of {2}"
          .format(field.name, field.type, field.length))

# print(fields[6])
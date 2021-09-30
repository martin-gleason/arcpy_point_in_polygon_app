import geocoder as gc
import unit_structure
import arcpy
g = gc.Geocoder()

a = '624 w 43rd place, chicago, il 60609'
b = '1422 E. 69th St, D, Chicago 60609'
c = '3920 W Huron	1-E	Chicago 60624'
d = '8854 South Yale Chicago 60620'
e = '5204 W Byron St 2nd FL, Chicago 60641'

addys = [a, b, c, d, e]

fields = arcpy.ListFields(g.shape_file)

points = []
for addy in addys:
    points.append(g.geocode_address(addy))

#
# for field in fields:
#     print("{0} is a type of {1} with a length of {2}"
#           .format(field.name, field.type, field.length))

with arcpy.da.SearchCursor(g.shape_file, ['SHAPE@', 'dist_num']) as cursor:
    for row in cursor:
        polygonGeom = row[0]
        #print(u'{0}, {1}, {2}'.format(row[0], row[1], row[2]))
        if polygonGeom.contains(points[0]):
            print('found')
            district = row[1]
            print(district)
        else:
            district = row[1]
            print(f'{district} issue:')


# #testing new locator
#
# def return_new_district(point, verbose = False):
#     district = ''
#     if point == None:
#         return f'Calcuated address does not appear to be in Cook county'
#     else:
#         field = 'dist_num'
#         with arcpy.da.SearchCursor(g.shape_file, ['SHAPE@', 'OID@', field]) as cursor:
#             for row in cursor:
#                 polygonGeom = row[0]
#                 if polygonGeom.contains(point):
#                     district = row
#                     print(len(district))
#                     print(district)
#         while verbose:
#             if len(district) >= 1:
#                 print(district)
#                 return district
#             elif len(district) < 1:
#                 return f'The result of the geocode: {district} indicates that the address appears to be in Cook County, but not in Chicago.'
#         else:
#             return district




city_units = unit_structure.load_units_to_class('units\list_of_units.json')

district = 12
for unit in city_units:
    if district in unit.get_police_district():
        print(unit.get_police_district())
        spo = unit.get_spo_name()
        break
    else:
        spo = 'Nope'
print(spo)


test = city_units[4]
print(test.get_spo_name())

print(test.get_supervisor(district))
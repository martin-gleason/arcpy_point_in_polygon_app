import os, sys, arcpy

#take an address, passed from another script, and geo code it. Return the points
address = '624 w 43rd Place, Chicago, IL 60609'
address2 = '736 terry lane, Countryside, IL, 60525'
address3 = '4936 s Forrestville, Chicago, IL 60622'
a4 = '2245 w ogden ave, chicago, il 60612'
police_16d = '5151 North Milwaukee Ave, chicago, il'

locator_path = r"C:\Users\Public\ArcGIS\ccjpdLocator\MyProject1\Address_Points_geojson.loc"
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


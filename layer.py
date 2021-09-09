import os, sys, arcpy

#first test: read layer file and print what's in it

locator_path = r"C:\Users\Public\ArcGIS\ccjpdLocator\MyProject1\Police Districts Chicago.lyrx"

lyrFile = arcpy.mp.LayerFile(locator_path)
for lyr in lyrFile.listLayers():
    print(lyr.name)
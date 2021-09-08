from flask import Flask
import arcgis
import geocoder

gc = geocoder.Geocoder()
print(gc)
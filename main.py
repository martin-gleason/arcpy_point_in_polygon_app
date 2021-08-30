import os, sys, arcpy
from test_addresses import addresses
from geocoder import Geocoder

gc = Geocoder()
address = addresses

print(address[1].get('address'))

gc.geocode_to_district(address = address[1].get('address'))

#gc.geocode_address()
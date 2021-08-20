#This is the code to geocode an address as a function

import arcpy

#if minscore becomes an issue, remember to: capture minimum score in function call, examing candidate for minscore, select highest score.
#which makes me thing I just need to capture highest score
# address will be verified in flask

def geocode(address, locator_path):
    locator = arcpy.geocoding.Locator(locator_path)
    candidate = locator.geocode(address, False)
    return [sub['Shape'] for sub in candidate][0]

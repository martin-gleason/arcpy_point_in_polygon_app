# Geocoder as a Service

This Cook County project is an attempt to create a microservice based on Esri's Arcpy. The service itself is built in Flask. 

The firstclass represents how addresses are received, geocoded, and placed within the proper polygon. Addresses, thus far, are not broken down into component parts; however, this may chance depending on locator accuracy.

Current instance methods are:
* get_district: string of address, return police district or NONE if none
* geocode_address: string address, return points
* get_shape_file: returns location to path of shape file
* set_shape_file: a function to add a shapefile for finding/adding locations
* return_district: takes an address point, returns numerical police district
* geocode_to_district: Takes an address, geocodes it, and then returns numerical police district


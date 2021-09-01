# Geocoder as a Service

This Cook County project is an attempt to create a microservice based on Esri's Arcpy. The service itself is built in Flask. In addition to the Arcpy code, another class called unit structure is created to help facilitate the assignment of youth to a particular geographic location. This should be based on the (CFive Supervisor)[https://www.cfive.com/products/supervisor/], but the initial version will be json files.

The first class represents how addresses are received, geocoded, and placed within the proper polygon. Addresses, thus far, are not broken down into component parts; however, this may chance depending on locator accuracy.

## Geocoder Class
Current instance methods are:
* get_district: string of address, return police district or NONE if none
* geocode_address: string address, return points
* get_shape_file: returns location to path of shape file
* set_shape_file: a function to add a shapefile for finding/adding locations
    This method isn't implemented yet, and is being created to help load new shapefiles as the needs of the Juvenile Probation Department change.
* return_district: takes an address point, returns numerical police district
* geocode_to_district: Takes an address, geocodes it, and then returns numerical police district

## Unit Structure Class
The parent class contains the following variables:
* spo_fname: SPO First Name
* spo_lname: SPO Last Name
* division: Division

A child class of Field Unit has also been created. Those variables include:
* court_date: Court dates as listed in the monthly roster
* police_district: Police districts covered by the field unit
* calendar: The court calendar covered by the unit
* division: The division the unit belongs to, in lieu of deputies

Both classes default the SPO first name to *officer*. 
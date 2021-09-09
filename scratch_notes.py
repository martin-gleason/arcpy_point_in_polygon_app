# %%

from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import unit_structure as office
import json
import geocoder

#load geocoder
gc = geocoder.Geocoder()

#load city units
city_units = office.load_units_to_class('units\list_of_units.json')

# %%

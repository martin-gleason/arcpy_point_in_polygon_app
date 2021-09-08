from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import unit_structure as office
import json
import geocoder

#load geocoder
gc = geocoder.Geocoder()

#load city units
#turns json file to list
city_units = office.load_units_to_class('units\list_of_units.json')


#load app
app = Flask(__name__)
api = Api(app)

class Units(Resource):
    def get(self):
        unit_list  = []
        for unit in city_units:
            unit_list.append(unit.__dict__)
        return unit_list

class GetDistrict(Resource):
    def get(self):
        pd = []
        for unit in city_units:
            pd.append(unit.get_police_district())
        return pd
        

# class GeoService(Resource, gc):
#     def get


api.add_resource(Units, '/units')
api.add_resource(GetDistrict, '/districts')
app.run(port=5000, debug=True)


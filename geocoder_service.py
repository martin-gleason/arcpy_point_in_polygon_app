import typing_extensions
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import unit_structure as office
import json
import address_parser as p
import geocoder

#load geocoder
gc = geocoder.Geocoder()


#load city units
#turns json file to list
city_units = office.load_units_to_class('units\list_of_units.json')

#load app
app = Flask(__name__)
api = Api(app)


#json parser being created as seperate class

class Units(Resource):
    def get(self):
        unit_list  = []
        for unit in city_units:
            unit_list.append(unit.__dict__)
        return unit_list

class GetDistrict(Resource):
    def get(self):
       parse = p.GetAddress(Resource)
       data = parse.parser.parse_args()
       district = gc.geocode_to_district(data['address'])
       return {'Police District': district}
        

class GeocodeAddress(Resource):
    def get(self):
        parse = p.GetAddress(Resource)
        data = parse.parser.parse_args()
        points = gc.geocode_address(data['address'])
        if points:
            return {'address': str(points)}
        else:
            return {'address': 'Address does not appear to be in Cook County'}
    

class AssignByAddress(Resource):
    def get(self):
        parse = p.GetAddress(Resource)
        data = parse.parser.parse_args()
        district = gc.geocode_to_district(data['address'])
        for unit in city_units:
            if unit.get_supervisor(int(district)):
                return {'supervisor': str(unit.spo_lname)}

        


api.add_resource(Units, '/units')
api.add_resource(GetDistrict, '/districts')
api.add_resource(GeocodeAddress, '/geocode/')
api.add_resource(AssignByAddress, '/assign/')
app.run(port=5000, debug=True)


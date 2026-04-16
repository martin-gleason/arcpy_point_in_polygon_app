import os

from flask import Flask
from flask_restful import Resource, Api

import address_parser as p
import geocoder
import unit_structure as office

UNITS_FILE = os.path.join(os.path.dirname(__file__), "units", "list_of_units.json")

gc = geocoder.Geocoder()
city_units = office.load_units_to_class(UNITS_FILE)

app = Flask(__name__)
api = Api(app)


class Units(Resource):
    def get(self):
        return [unit.__dict__ for unit in city_units]


class GetDistrict(Resource):
    def get(self):
        data = p.GetAddress.parser.parse_args()
        district = gc.geocode_to_district(data["address"])
        return {"Police District": district}


class GeocodeAddress(Resource):
    def get(self):
        data = p.GetAddress.parser.parse_args()
        point = gc.geocode_address(data["address"])
        if point is None:
            return {"address": "Address does not appear to be in Cook County"}
        return {"address": str(point)}


class AssignByAddress(Resource):
    def get(self):
        data = p.GetAddress.parser.parse_args()
        district = gc.geocode_to_district(data["address"])
        if not isinstance(district, int):
            return {"supervisor": None, "reason": district}
        for unit in city_units:
            if unit.get_supervisor(district):
                return {"supervisor": unit.spo_lname}
        return {"supervisor": None, "reason": f"No unit covers district {district}"}


api.add_resource(Units, "/units")
api.add_resource(GetDistrict, "/districts")
api.add_resource(GeocodeAddress, "/geocode/")
api.add_resource(AssignByAddress, "/assign/")


if __name__ == "__main__":
    app.run(port=5000)

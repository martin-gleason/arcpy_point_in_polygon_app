import typing_extensions
from flask import Flask, jsonify, request, render_template, flash
from flask_restful import Resource, Api, reqparse, fields, marshal_with

from flask_wtf.csrf import CSRFProtect, CSRFError
import unit_structure as office
import json
import address_parser as p
import geocoder
import gis_forms

#load geocoder
gc = geocoder.Geocoder()

#Secret Key: have to make more secure
SECRET_KEY='SECRET TO EVERYBODY'

#load city units
#turns json file to list
city_units = office.load_units_to_class('units\list_of_units.json')

#load app
SESSION_COOKIE_SECURE = True
app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)
csrf = CSRFProtect()
csrf.init_app(app)

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

        


@app.context_processor
def geocoder_version():
    return dict(shape_file=gc.get_shape_file())

@app.route('/', methods=['GET', 'POST'])
def index():
    spo = ''
    form = gis_forms.AddressForm()
    street = request.form.get('street')
    line2 = request.form.get('address_line2')
    city = request.form.get('city')
    state = request.form.get('state')
    zip = request.form.get('zip')
    zip4 = request.form.get('zip4')

    if form.validate_on_submit():
        if zip4:
            address = street + " " + line2 + " " + city + ", " + state.upper() + " "+ zip + "+" + zip4
        else:
            address = street + " " + line2 + " " + city + ", " + state.upper() + " " + zip

        district = gc.geocode_to_district(address)
        print(district)

        for unit in city_units:
            if unit.get_supervisor(district):
                spo = unit.get_spo_name()
                break
            else:
                spo = 'Nope'

        flash(f"The Police District is: {district} ")
        #
        # ) + \
        #       f". And the SPO is: {spo}")

    else:
        print('Failed to validate.')
        print(form.errors)

    return render_template('index.html', form=form)


#rest endpoints for consumption
api.add_resource(Units, '/units')
api.add_resource(GetDistrict, '/getdistrict')
api.add_resource(GeocodeAddress, '/geocode/')
api.add_resource(AssignByAddress, '/assign/')
app.run(port=5000, debug=True)


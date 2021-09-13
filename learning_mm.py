#learning Marshmallow 3.13
from typing import Union
from marshmallow import Schema, fields
import marshmallow
import unit_structure as office
import pprint


city_units = office.load_units_to_class('units\list_of_units.json')

class UnitSchema(Schema):
    spo_lname = fields.Str()
    spo_fname = fields.Str()
    court_date =  fields.List(marshmallow.fields.Str(), cls_or_instance=)
    police_district = fields.List(marshmallow.fields.Str(), many=True)
    calendar = fields.List(marshmallow.fields.Str(), many=True)
    division = fields.Int()

schema = UnitSchema()



#result = schema.dump(city_units[1])

units = []

for unit in city_units:
     units.append(schema.dump(unit))




#print(type(result))
print(city_units[1])
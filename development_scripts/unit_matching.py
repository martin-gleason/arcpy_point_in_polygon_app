import unit_structure as units

city_units = units.load_units_to_class(r'..\units\list_of_units.json')

for unit in city_units:
    print(unit.get_police_district())

for unit in city_units:
    if 4 in unit.get_police_district():
        print(unit.get_spo_name())
    else:
        print('not found')





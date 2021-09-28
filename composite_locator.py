import geocoder as gc
import unit_structure
g = gc.Geocoder()



city_units = unit_structure.load_units_to_class('units\list_of_units.json')

district = 12
for unit in city_units:
    if district in unit.get_police_district():
        print(unit.get_police_district())
        spo = unit.get_spo_name()
        break
    else:
        spo = 'Nope'
print(spo)


test = city_units[4]
print(test.get_spo_name())

print(test.get_supervisor(district))
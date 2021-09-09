import unit_structure as u
#def __init__(self, spo_lname: str,  court_date: list, police_district: Union[str, int, tuple], calendar: Union[str, int, tuple], division = 4, spo_fname:str = 'Officer'):


leanne = u.FieldUnit('Engleman', ['Thursday', 'Tuesday'], police_district=(14, 17, 18, 19, 20, 24), calendar=(58, 60), spo_fname='Leanne')
randy = u.FieldUnit('Garcia', ['Tuesday'], police_district=(16, 25), calendar=58, spo_fname='Randy')
karen = u.FieldUnit('Jouras', ['Wednesday'], police_district=(7, ), calendar=55, spo_fname='Karen')
marshawna = u.FieldUnit('Moore', ['Tuesday'], police_district=(5, ), calendar=52, spo_fname='Marshawna')
rich = u.FieldUnit('Naujokas', ['Tuesday'], police_district=(8, ), calendar=53, spo_fname='Richard')
aaron = u.FieldUnit('Campbell', ['Thursday'], police_district=(11, ), calendar=57, spo_fname='Aaron')
kelly = u.FieldUnit('Flanagan', ['Tuesday'], police_district=(1, 2, 12, 21), calendar=(55, 60, 63), spo_fname='Kelly')
carolyn = u.FieldUnit('Hopkins', court_date=['Tuesday'], police_district=(3, ), calendar=[68], spo_fname='Carolyn')
steve = u.FieldUnit('Kasperski', ['Wednesday'], police_district=(9, ), calendar=63, spo_fname='Steve')
chris = u.FieldUnit('LeMay', court_date=['Wednesday'], police_district=(4, ), calendar=52, spo_fname='Chris')
antwan = u.FieldUnit('Jones',  court_date=['Wednesday'], police_district=(15, ), calendar=53, spo_fname='Antwan')
lloyd = u.FieldUnit('Marshall', court_date=['Thursday'], police_district=(2, ), calendar=55, spo_fname='Lloyd')

chicago_field = [leanne, randy, karen, marshawna, rich, aaron, kelly, carolyn, steve, chris, antwan, lloyd]

fields = u.list_of_units(leanne, randy, karen, marshawna, rich, aaron, kelly, carolyn, steve, chris, antwan, lloyd)

u.write_unit_to_json(fields)
division_4 = u.load_units_to_class('units/list_of_units.json')

for unit in division_4:
    print(unit)

print(division_4[0].get_supervisor(18))


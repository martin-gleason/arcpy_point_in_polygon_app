""""
This is a class used to assign officers based on police districts.
"""

import json
import os
from pathlib import Path
from typing import Union



class UnitStructure:
    # unit_structure = {'Division': '', '
    # Unit Name': '',
    # 'Court Date': ,
    # 'Police District': (),
    # 'SPO First Name': '',
    # 'Calendar': ()}

    def __init__(self, spo_lname: str, division=4, spo_fname:str= 'Officer'):
        self.division = division
        self.spo_lname = spo_lname
        self.spo_fname = spo_fname

    def __str__(self):
        return f"SPO {self.spo_lname}."

    def set_division(self, division: int):
        self.division = division
        return f'The new division is {division}'

    def set_spo(self, spo_lname: str):
        self.spo_lname = spo_lname
        return f'The new SPO is SPO {self.spo_lname}'

    def get_spo_name(self):
        return f'The Supervisor is {self.spo_fname} {self.spo_lname}'

class FieldUnit(UnitStructure):
    def __init__(self, spo_lname: str,  court_date: list, police_district: Union[str, int, tuple], calendar: Union[str, int, tuple], division = 4, spo_fname:str = 'Officer'):
       super().__init__(spo_lname, division, spo_fname)
       self.court_date = court_date
       self.police_district = police_district
       self.cal = calendar
    
    def __str__(self):
        return (f'Superivisor {self.spo_lname} is in the {self.division} division, ' \
            f'and has covers the following police district(s): {self.police_district}. ' \
            f'Court is in {self.cal} on the following days: {self.court_date}')

def list_of_units(*units):
    list_of_units = []
    for unit in units:
        list_of_units.append(unit.__dict__)
    return list_of_units

def write_unit_to_json(list_of_units:[]):
    with open(os.path.join('units', 'list_of_units.json'), 'w') as f:
        for unit in list_of_units:
            json.dump(unit, f)
            f.write('\n')

#the next function will take the saved filed and load it into a class
def load_units():
    return 'not developed yet'

generic = UnitStructure('Riveria')
lele = FieldUnit(spo_lname = 'Engelman', court_date = ['Tuesday', 'Cal 58', 'Thursday', 'Cal 60'], police_district = (16, 22), calendar = (58, 60))

marty = FieldUnit(spo_lname = 'Gleason', court_date = ['Wednesay', 'Cal 55'], police_district = (9), calendar = (55, ))
joe = FieldUnit(spo_lname='Pacelt', court_date = ['Wednesay', 'Cal 55'], police_district = (9), calendar = (55, ))

print(lele)
print(marty.__dict__)
print(generic)
print(joe)

x = list_of_units(lele, marty, joe)

write_unit_to_json(x)
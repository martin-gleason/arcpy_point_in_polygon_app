""""
This is a class used to assign officers based on police districts.
    # unit_structure = {'Division': '', '
    # Unit Name': '',
    # 'Court Date': ,
    # 'Police District': (),
    # 'SPO First Name': '',
    # 'Calendar': ()}

"""

import json
import os
from pathlib import Path
from typing import Union

class UnitStructure:

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
       self.calendar = calendar
    
    def __str__(self):
        return (f'Superivisor {self.spo_lname} is in the {self.division} division, ' \
            f'and has covers the following police district(s): {self.police_district}. ' \
            f'Court is in {self.calendar} on the following days: {self.court_date}')

    def get_police_district(self):
        return self.police_district
    
    def get_supervisor(self, district: Union[int, str]):
        if district in self.police_district:
            return self.get_spo_name()

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

def load_units(file):
    units = []
    with open(os.path.relpath(file), 'r') as f:
        for unit in f:
            units.append(json.loads(unit))
    return units


def load_units_to_class(file):
    units = []
    with open(os.path.relpath(file), 'r') as f:
        for unit in f:
            temp_unit = json.loads(unit)
            units.append(FieldUnit(**temp_unit))
    return units
    
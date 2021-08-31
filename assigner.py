""""
This is a class used to assign officers based on police districts.
"""

from typing import Union

class unit_structure:
    #unit_structure = {'Division': '', '
    # Unit Name': '',
    # 'Court Date': ,
    # 'Police District': (),
    # 'SPO First Name': '',
    # 'Calendar': ()}


    def __init__(self, spo_name: str, court_date: list, police_district: Union[str, int, tuple], calendar: Union[str, int, tuple], division = 4):
        self.pd = police_district
        self.court = court_date
        self.division = division
        self.unit_name = 'SPO' + spo_name +  " Calendars: "+ str(calendar)
        self.spo_name = spo_name
        self.cal = calendar

    def __str__(self):
        return f"SPO {self.spo_name} has court on {self.court}.//n Court is {self.court}./n"
    def set_division(self, division: int):
        self.division = division
        return f'The new division is {division}'

    def set_spo(self, spo_name: str):
        self.spo_name = spo_name
        return f'The new SPO is SPO {spo_name}'




test = unit_structure(spo_name= 'Engelman', court_date= ['Tuesday', 'Cal 58', 'Thursday', 'Cal 60'], police_district = (16, 22), calendar = (58, 60))

print(test.set_spo('Gleason'))
print(test.spo_name)
print(test)

from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField
import re


class AddressForm(FlaskForm):
    #From https://stackoverflow.com/questions/30940323/python-make-sure-address-matches-specific-format.
    #maybe the best regex explation I've ever seen.
    #this verifies the address field

    street_verification=re.compile(r"""
    (?P<HouseNumber>\d+)\s+' 
    (?P<Direction>[news])\s+'
    (?P<StreetName>\w+)\s+'
    (?P<StreetDesignator>\w+),\s+
    """, flags=re.IGNORECASE | re.X)

    address_verification=re.compile(r'''
    (?P<HouseNumber>\d+)\s+' 
    (?P<Direction>[news])\s+'
    (?P<StreetName>\w+)\s+'
    (?P<StreetDesignator>\w+),\s+, '
    (?P<TownName>.*),\s+, '
    (?P<State>[A-Z]{2}),?\s+, '
    (?P<ZIP>\d{5})
    ''', flags=re.IGNORECASE | re.X)

    street = StringField('address')
    address_line2 = StringField('address_line2')
    city = StringField('city', validators=[validators.InputRequired()])
    state = StringField('state', validators=[validators.InputRequired()])
    zip = StringField('zip', validators=[validators.InputRequired()])
    zip4 = StringField('zip4')

    submit = SubmitField('Submit')

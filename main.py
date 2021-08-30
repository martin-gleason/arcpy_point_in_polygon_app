from test_addresses import addresses
from geocoder import Geocoder

gc = Geocoder()
address = addresses

terry_ln = gc.geocode_address(address[1].get('address'))

print(gc.return_district(terry_ln, verbose = True))

print(gc.geocode_to_district(address[0].get('address')))

print('district is: ' + str(gc.geocode_to_district('5410 S Wood, Chicago, Il')))

gc.geocode_to_district('5410 S Wood, Chicago, Il')
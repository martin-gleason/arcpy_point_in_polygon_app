#This is the parser. made as a sperate class to addrss the problem wtih flask restful

from flask_restful import reqparse 
import marshmallow


class GetAddress:
    def __init__(self, resource):
        self.resource = resource
    
    parser = reqparse.RequestParser()
    parser.add_argument('address',
        type = str,
        required=True,
        help="This field cannot be left blank"
    )
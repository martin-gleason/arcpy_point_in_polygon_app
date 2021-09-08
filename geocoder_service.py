from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse
import unit_structure as u
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'poguemahone'
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth; send username, password

items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' lready exists.".format(name)}, 400

        data = request.get_json()
        items.append(item)
        return item

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted.'}


    def put(self, name):
        parser = reqparse.RequestParser() #can go through fields in a form like in json payload
        parser.add_argument('price', 
            type = float,
            required=True,
            help='This Field cannot be left blank!'
        )

        data = parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else: 
            item.update(data)
        return item
        

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')



app.run(port=5000, debug=True)


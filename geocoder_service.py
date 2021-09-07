from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
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
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

    def post(self, name):
        data = request.get_json(force=True) #do not need content type header to be set to application/json; dangerous.
       #data = request.get_json(silent==True) #returns none
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return{'items': item}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')



app.run(port=5000, debug=True)


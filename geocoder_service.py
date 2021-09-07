from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
import unit_structure as u

app = Flask(__name__)
api = Api(app)

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return{'items': item}

api.add_resource(item, 'item/<string:name>')



app.run(port=5000, debug=True)


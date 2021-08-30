from flask import Flask, jsonify, request, render_template
import geocoder

app = Flask(__name__)

stores = [
    {
        'name': 'City Store',
        'items':[
            {
                'name': 'Pen',
                'price': 125.00

            }
        ]
    },
    {
        'name': 'Suburban Store',
        'items':[
            {
                'name': 'Overpriced Pen',
                'price': 165.00

            }
        ]
    }
]



@app.route('/') #homepage or endpoint?
def home():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store_name(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'stores': stores})
            

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item():
    reaquest_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)

@app.route('/store/<string:name>/item')
def get_item_in_store():
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})











app.run(port=5000)


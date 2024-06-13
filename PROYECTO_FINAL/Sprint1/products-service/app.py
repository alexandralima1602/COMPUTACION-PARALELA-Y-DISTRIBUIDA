from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
	products = [{'id': 1, 'name': 'Producto 1', 'price': 10.99},
            	{'id': 2, 'name': 'Producto 2', 'price': 15.50}]
	return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
	product = {'id': product_id, 'name': 'Producto 1', 'price': 10.99}
	return jsonify(product)

@app.route('/products', methods=['POST'])
def create_product():
	data = request.json
	return jsonify({'id': 3, 'name': data['name'], 'price': data['price']}), 201

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
	return jsonify({'status': 'OK'})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5002, debug=True)

from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Configuración de MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client.products_db
products_collection = db.products

@app.route('/products', methods=['GET'])
def get_products():
	products = list(products_collection.find())
	for product in products:
    	product['_id'] = str(product['_id'])
	return jsonify(products)

@app.route('/products', methods=['POST'])
def create_product():
	data = request.get_json()
	product = products_collection.insert_one(data)
	return jsonify({'_id': str(product.inserted_id)}), 201

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
	product = products_collection.find_one({'_id': ObjectId(product_id)})
	if not product:
    	return jsonify({'error': 'Producto no encontrado'}), 404
	product['_id'] = str(product['_id'])
	return jsonify(product)

@app.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
	data = request.get_json()
	result = products_collection.update_one({'_id': ObjectId(product_id)}, {'$set': data})
	if result.modified_count == 0:
    	return jsonify({'error': 'Producto no encontrado'}), 404
	return jsonify({'message': 'Producto actualizado exitosamente'})

@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
	result = products_collection.delete_one({'_id': ObjectId(product_id)})
	if result.deleted_count == 0:
    	return jsonify({'error': 'Producto no encontrado'}), 404
	return jsonify({'message': 'Producto eliminado exitosamente'})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5002) 


from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
	orders = [{'id': 1, 'user_id': 1, 'total': 25.99},
          	{'id': 2, 'user_id': 2, 'total': 48.75}]
	return jsonify(orders)

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
	order = {'id': order_id, 'user_id': 1, 'total': 25.99}
	return jsonify(order)

@app.route('/orders', methods=['POST'])
def create_order():
	data = request.json
	return jsonify({'id': 3, 'user_id': data['user_id'], 'total': data['total']}), 201

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
	return jsonify({'status': 'OK'})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5004, debug=True)

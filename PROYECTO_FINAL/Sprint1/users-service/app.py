from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
	users = [{'id': 1, 'name': 'John Doe'}, {'id': 2, 'name': 'Jane Doe'}]
	return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
	user = {'id': user_id, 'name': 'John Doe'}
	return jsonify(user)

@app.route('/users', methods=['POST'])
def create_user():
	data = request.json
	return jsonify({'id': 3, 'name': data['name']}), 201

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
	return jsonify({'status': 'OK'})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001, debug=True)

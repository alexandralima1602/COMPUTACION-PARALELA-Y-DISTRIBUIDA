from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
	username = request.json['username']
	password = request.json['password']
	# Aquí iría la lógica de autenticación
	return jsonify({'token': 'abc123'})

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
	return jsonify({'status': 'OK'})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)

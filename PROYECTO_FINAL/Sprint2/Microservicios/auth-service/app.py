from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
# Diccionario para almacenar usuarios
users = {}
@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']

	if username not in users:
    	return jsonify({'error': 'Credenciales inválidas'}), 401

	if not check_password_hash(users[username], password):
    	return jsonify({'error': 'Credenciales inválidas'}), 401

	return jsonify({'message': 'Inicio de sesión exitoso'})

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']

	if username in users:
    	return jsonify({'error': 'Usuario ya existe'}), 400

	users[username] = generate_password_hash(password)
	return jsonify({'message': 'Usuario registrado exitosamente'})

@app.route('/logout', methods=['POST'])
def logout():
	# Aquí se implementaría la lógica para cerrar sesión
	return jsonify({'message': 'Sesión cerrada exitosamente'})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)


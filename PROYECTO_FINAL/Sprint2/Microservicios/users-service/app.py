from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

# Configuración de la base de datos
engine = create_engine('postgresql://user:password@localhost:5432/users_db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Definición del modelo de usuario
class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	email = Column(String, unique=True)

@app.route('/users', methods=['GET'])
def get_users():
	session = Session()
	users = session.query(User).all()
	return jsonify([user.to_dict() for user in users])

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	session = Session()
	user = User(name=data['name'], email=data['email'])
	session.add(user)
	session.commit()
	return jsonify(user.to_dict()), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
	session = Session()
	user = session.query(User).get(user_id)
	if not user:
    	return jsonify({'error': 'Usuario no encontrado'}), 404
	return jsonify(user.to_dict())

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
	data = request.get_json()
	session = Session()
	user = session.query(User).get(user_id)
	if not user:
    	return jsonify({'error': 'Usuario no encontrado'}), 404
	user.name = data['name']
	user.email = data['email']
	session.commit()
	return jsonify(user.to_dict())

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
	session = Session()
	user = session.query(User).get(user_id)
	if not user:
    	return jsonify({'error': 'Usuario no encontrado'}), 404
	session.delete(user)
	session.commit()
	return jsonify({'message': 'Usuario eliminado exitosamente'})

if __name__ == '__main__':
	Base.metadata.create_all(engine)
	app.run(debug=True, host='0.0.0.0', port=5001)


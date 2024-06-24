from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from products_service import get_product_price

app = Flask(__name__)

# Configuración de la base de datos
engine = create_engine('postgresql://user:password@localhost:5432/orders_db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Definición del modelo de pedido
class Order(Base):
	__tablename__ = 'orders'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer)
	product_id = Column(Integer)
	quantity = Column(Integer)
	total = Column(Float)

@app.route('/orders', methods=['GET'])
def get_orders():
	session = Session()
	orders = session.query(Order).all()
	return jsonify([order.to_dict() for order in orders])

@app.route('/orders', methods=['POST'])
def create_order():
	data = request.get_json()
	session = Session()
	total = calculate_total(data['product_id'], data['quantity'])
	order = Order(user_id=data['user_id'], product_id=data['product_id'], quantity=data['quantity'], total=total)
	session.add(order)
	session.commit()
	return jsonify(order.to_dict()), 201

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
	session = Session()
	order = session.query(Order).get(order_id)
	if not order:
    	return jsonify({'error': 'Pedido no encontrado'}), 404
	return jsonify(order.to_dict())

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
	data = request.get_json()
	session = Session()
	order = session.query(Order).get(order_id)
	if not order:
    	return jsonify({'error': 'Pedido no encontrado'}), 404
	order.user_id = data['user_id']
	order.product_id = data['product_id']
	order.quantity = data['quantity']
	order.total = calculate_total(data['product_id'], data['quantity'])
	session.commit()
	return jsonify(order.to_dict())

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
	session = Session()
	order = session.query(Order).get(order_id)
	if not order:
    	return jsonify({'error': 'Pedido no encontrado'}), 404
	session.delete(order)
	session.commit()
	return jsonify({'message': 'Pedido eliminado exitosamente'})

def calculate_total(product_id, quantity):
	product_price = get_product_price(product_id)
	if product_price is None:
    	return 0.0
	return product_price * quantity

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5004)


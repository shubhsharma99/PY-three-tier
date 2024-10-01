from flask import Flask, request, jsonify
from config import Config
from models import db, Customer, Product
from services import create_customer, get_customers, create_product, get_products

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    customer = create_customer(data['first_name'], data['last_name'])
    return jsonify({'id': customer.CustomerId}), 201

@app.route('/customers', methods=['GET'])
def list_customers():
    customers = get_customers()
    return jsonify([{'id': c.CustomerId, 'first_name': c.CustomerFirstName, 'last_name': c.CustomerLastName} for c in customers])

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    product = create_product(data['name'])
    return jsonify({'id': product.ProductId}), 201

@app.route('/products', methods=['GET'])
def list_products():
    products = get_products()
    return jsonify([{'id': p.ProductId, 'name': p.ProductName} for p in products])

if __name__ == '__main__':
    app.run(debug=True)

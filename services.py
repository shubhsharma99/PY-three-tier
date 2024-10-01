from models import db, Customer, Product

def create_customer(first_name, last_name):
    new_customer = Customer(CustomerFirstName=first_name, CustomerLastName=last_name)
    db.session.add(new_customer)
    db.session.commit()
    return new_customer

def get_customers():
    return Customer.query.all()

def create_product(name):
    new_product = Product(ProductName=name)
    db.session.add(new_product)
    db.session.commit()
    return new_product

def get_products():
    return Product.query.all()

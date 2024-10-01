from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'Customer'
    
    CustomerId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CustomerFirstName = db.Column(db.String(255))
    CustomerLastName = db.Column(db.String(255))

class Product(db.Model):
    __tablename__ = 'Product'
    
    ProductId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ProductName = db.Column(db.String(255))

from models.db import db

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(50))
    current_price = db.Column(db.Float)
    available_quantity = db.Column(db.Integer)
    description = db.Column(db.String(50))

    ingredients = db.relationship('Ingredient', back_populates = "products", secondary='product_ingredients')
    orders = db.relationship('Order', backref='products')

from app import db  # Используем db из app/__init__.py

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=True)
    old_price = db.Column(db.Float, nullable=True)
    image_url = db.Column(db.String(100), nullable=True)
    is_best_seller = db.Column(db.Boolean, default=False)
    texture_url = db.Column(db.String(255), nullable=True)
    composition = db.Column(db.Text, nullable=True)
    certificates = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Product('{self.name}', '{self.price}')"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'old_price': self.old_price,
            'image_url': self.image_url,
            'is_best_seller': self.is_best_seller,
            'texture_url': self.texture_url,
            'composition': self.composition,
            'certificates': self.certificates,
        }

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(200), nullable=False)

    product = db.relationship('Product', backref='orders', lazy=True)

    def __repr__(self):
        return f"Order('{self.product.name}', '{self.quantity}')"


class CooperationFormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    message = db.Column(db.Text)

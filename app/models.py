from app import db
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return f'<User {self.name}>'
    
class todos(db.Model):
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=True)
    todo = db.Column(db.String(230), nullable=False)
    description = db.Column(db.String(230), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Todo {self.todo}>'

class product(db.Model):
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=True)
    product = db.Column(db.String(230), nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return f'<Product {self.product}>'
    
class katergori_product(db.Model):
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=True)
    product_id = db.Column(db.BigInteger, db.ForeignKey('product.id'), nullable=False)
    kategori = db.Column(db.String(230), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return f'<Kategori {self.kategori}>'

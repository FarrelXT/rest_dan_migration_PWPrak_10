from app.modelele import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def setpassword(self, password):
        self.password = generate_password_hash(password)

    def checkpass(self, password):
        return check_password_hash(self.password, password)

    # def __repr__(self):
    #     return f'<User {self.name}>'
    # DIRUBAH MENJADI ==> 
    def __repr__(self):
        return '<User {}>'.format(self.name)


#PERPINDAHAN LINE CODE KE FILE ===> (todos_modelele.py)

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
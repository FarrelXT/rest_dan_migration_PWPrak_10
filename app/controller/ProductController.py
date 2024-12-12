from app.modelele.model import product
from app import response
from flask import request
from app.modelele import db

def index():
    try:
        products = product.query.all()
        data = transform(products)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def transform(products):
    array = []
    for product in products:
        array.append({
            'id': product.id,
            'product': product.product,
            'price': product.price,
            'created_at': product.created_at,
            'updated_at': product.updated_at
        })
    return array

def show(id):
    try:
        Product = product.query.filter_by(id=id).first()
        if not Product:
            return response.badReq([], 'Data Tidak Ditemukan')
        data = single_transform(Product)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def single_transform(Product):
    data = {
        'id': Product.id,
        'product': Product.product,
        'price': Product.price,
        'created_at': Product.created_at,
        'updated_at': Product.updated_at
    }
    return data

def store():
    try:
        product_name = request.json['product']
        price = request.json['price']
        Product = product(product=product_name, price=price)
        db.session.add(Product)
        db.session.commit()

        return response.ok('', 'Berhasil menambahkan data')
    except Exception as e:
        print(e)

def update(id):
    try:
        product_name = request.json['product']
        price = request.json['price']

        Product = product.query.filter_by(id=id).first()
        Product.product = product_name
        Product.price = price

        db.session.commit()
        return response.ok('', 'Berhasil mengupdate data')
    except Exception as e:
        print(e)

def delete(id):
    try:
        Product = product.query.filter_by(id=id).first()
        if not Product:
            return response.badReq([], 'Data Tidak Ditemukan')
        db.session.delete(Product)
        db.session.commit()

        return response.ok('', 'Berhasil menghapus data')
    except Exception as e:
        print(e)
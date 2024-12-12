from app.modelele.model import katergori_product
from app import response
from flask import request
from app.modelele import db

def index():
    try:
        categories = katergori_product.query.all()
        data = transform(categories)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def transform(categories):
    array = []
    for category in categories:
        array.append({
            'id': category.id,
            'product_id': category.product_id,
            'kategori': category.kategori,
            'created_at': category.created_at,
            'updated_at': category.updated_at
        })
    return array

def show(id):
    try:
        category = katergori_product.query.filter_by(id=id).first()
        if not category:
            return response.badReq([], 'Data Tidak Ditemukan')
        data = single_transform(category)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def single_transform(category):
    data = {
        'id': category.id,
        'product_id': category.product_id,
        'kategori': category.kategori,
        'created_at': category.created_at,
        'updated_at': category.updated_at
    }
    return data

def store():
    try:
        product_id = request.json['product_id']
        kategori = request.json['kategori']
        category = katergori_product(product_id=product_id, kategori=kategori)
        db.session.add(category)
        db.session.commit()

        return response.ok('', 'Berhasil menambahkan data')
    except Exception as e:
        print(e)

def update(id):
    try:
        product_id = request.json['product_id']
        kategori = request.json['kategori']

        category = katergori_product.query.filter_by(id=id).first()
        category.product_id = product_id
        category.kategori = kategori

        db.session.commit()
        return response.ok('', 'Berhasil mengupdate data')
    except Exception as e:
        print(e)

def delete(id):
    try:
        category = katergori_product.query.filter_by(id=id).first()
        if not category:
            return response.badReq([], 'Data Tidak Ditemukan')
        db.session.delete(category)
        db.session.commit()

        return response.ok('', 'Berhasil menghapus data')
    except Exception as e:
        print(e)
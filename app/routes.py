# from app.modelele.model import Users
from app.controller import UserController
from app.modelele import app
from flask import request

# TAMBAHAN UNTUK AKSES "model.py" dan "todos_modelele.py" dari modelele folder
@app.route('/users')
def user():
    return UserController.index()

# TAMBAHAN AKSES UNTUK "def tampilkan()...." dari UserController.py
# GUNA ROUTING user BERDASARKAN id
# method POST untuk menyimpan data dan menampilkan data yang telah di simpan
# method GET untuk menampilkan data yang telah di simpan
# TAMBAHAN AKSES UNTUK "def store()...." dari UserController.py
@app.route('/users/<id>', methods=['POST', 'GET', 'DELETE', 'PUT'])
def usersDETAIL(id):
    if request.method == 'GET':
        return UserController.index(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    else:
        return UserController.store(id)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

# TUUGAS 9.5
from app.controller import ProductController

@app.route('/products', methods=['POST', 'GET'])
def products():
    if request.method == 'GET':
        return ProductController.index()
    else:
        return ProductController.store()

@app.route('/products/<id>', methods=['GET', 'PUT', 'DELETE'])
def product_detail(id):
    if request.method == 'GET':
        return ProductController.show(id)
    elif request.method == 'PUT':
        return ProductController.update(id)
    else:
        return ProductController.delete(id)
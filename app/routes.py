# from app.modelele.model import Users
from app.controller import UserController
from app.modelele import app
from flask import request

# TAMBAHAN UNTUK AKSES "model.py" dan "todos_modelele.py" dari modelele folder
# @app.route('/users')
# def users():
#     return UserController.index()


# TAMBAHAN AKSES UNTUK "def tampilkan()...." dari UserController.py
# GUNA ROUTING user BERDASARKAN id
@app.route('/users/<id>')
def user(id):
    return UserController.tampilkan(id)

# method POST untuk menyimpan data dan menampilkan data yang telah di simpan
# method GET untuk menampilkan data yang telah di simpan
# TAMBAHAN AKSES UNTUK "def store()...." dari UserController.py
@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.store()

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
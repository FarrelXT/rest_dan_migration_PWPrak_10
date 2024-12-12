from app.modelele.model import Users
from app import response 
# tambahan import untuk request dan db di password
from flask import request
from app.modelele import db


def index():
    try:
        users = Users.query.all()
        data =  transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)


def transform(users):
    array = []
    for a in users :
        array.append({
            'id' : a.id,
            'name': a.name,
            'email': a.email,
            'created_at': a.created_at,
            'updated_at': a.updated_at
        })
    return array 
     
# jika ingin mendapatkan hasil ID menggunakan fungsi GET maka gunakaan metode "tampilkan" dengan parameter id
def tampilkan(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], 'Data Tidak Ditemukan')
        data = singleTransform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e) 


# untuk "def tampilkan()...... data = singleTransform(users)...."
def singleTransform(user):
    data = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'created_at': user.created_at,
        'updated_at': user.updated_at
    }
    return data

def update(id):
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        users = Users.query.filter_by(id=id).first()
        users.name = name
        users.email = email
        users.setpassword(password)

        db.session.commit()
        return response.ok('', 'berasil update')
    except Exception as e:
        print(e)

def delete(id):
    try :
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], 'Data Tidak Ditemukan')
        db.session.delete(users)        
        db.session.commit()

        return response.ok('', 'Berhasil hapus data')
    except Exception as e:
        print(e)

def store():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        users = Users(name=name, email=email)
        users.setpassword(password)
        db.session.add(users)
        db.session.commit()

        return response.ok('', 'Berhasil menambahkan data')
    except Exception as e:
        print(e)
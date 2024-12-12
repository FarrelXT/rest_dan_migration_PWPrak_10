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
            'email': a.email
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
        'email': user.email
    }
    return data



def store():
    try:
        id = request.json['id']
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        users = Users(id=id ,name=name, email=email)
        users.setpassword(password)
        db.session.add(users)
        db.session.commit()

        return response.ok('', 'Berhasil menambahkan data')
    except Exception as e:
        print(e)
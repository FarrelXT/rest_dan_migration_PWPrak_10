# file yang akan di keluarkan saat ada request dari client, dan respoone gagal atau berhasilnya
# sebuah request yang diminta oleh client berupa json yang diminta dari server.

from flask import jsonify, make_response
def ok(values, message):
    return make_response(jsonify({
        'status': 'ok',
        'message': message,
        'data': values
    }), 200)

def badReq(values, message):
    return make_response(jsonify({
        'status': 'bad request',
        'message': message,
        'data': values
    }), 400)
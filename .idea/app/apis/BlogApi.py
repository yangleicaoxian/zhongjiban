from flask import jsonify
from flask_restful import Resource, reqparse

from app.models import db
from app.apis.UserApi import parser

parser = reqparse.RequestParser()
parser.add_argument(name='name', type=str, required=True, help='用户名必须填写')
parser.add_argument(name='email', type=str, required=True, help='用户邮箱必须填写')
parser.add_argument(name='password', type=str, required=True, help='用户邮箱必须填写')
parser.add_argument(name='telephone', type=str, required=True, help='用户手机号必须填写')


class B_Register(Resource):
    def post(self):
        parse = parser.parse_args()
        telephone = parse.get('telephone')
        email = parse.get('email')
        name = parse.get('name')
        data = {
            'msg': '博客注册成功',

            'status': '200',

        }
        bg = Blog()
        bg.telephone = telephone,
        bg.email = email
        bg.name = name
        db.session.add(bg)
        db.session.commit()
        return jsonify(data)


class B_Modify(Resource):
    def post(self):
        data = {
            'msg': '修改成功'
        }
        bg = Blog.query.get(1)
        bg.name = 'zs'
        db.session.add(bg)
        db.session.commit()
        return jsonify(data)


class B_Del(Resource):
    def post(self):
        data = {
            'msg': '删除成功'
        }
        bg = Blog.query.get(1)
        db.session.delete(bg)
        db.session.commit()

        return jsonify(data)

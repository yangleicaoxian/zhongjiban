from flask import jsonify
from flask_restful import Resource, reqparse

from app.models import User,db

parser = reqparse.RequestParser()
parser.add_argument(name='email',type=str,required=True,help='用户邮箱必须填写')
parser.add_argument(name='password',type=str,required=True,help='用户密码必须填写')
parser.add_argument(name='name',type=str,required=True,help='用户名字必须填写')


class Register(Resource):
    def post(self):
        parse = parser.parse_args()
        password=parse.get('password')
        email = parse.get('email')
        name=parse.get('name')
        data={
            'msg':'注册成功',

            'status':'200',

        }
        user=User()
        user.password=password,
        user.email=email
        user.name=name
        db.session.add(user)
        db.session.commit()
        return jsonify(data)



class Login(Resource):
    def post(self):
        parse = parser.parse_args()

        email = parse.get('email')
        password = parse.get('password')
        name=parse.get('name')

        users = User.query.filter(User.name .__eq__(name))

        if users.count()>0:
            user =users.first()
            if user.email==email and user.password==password:

                return {'msg':'OK'}
            else:
                return {'msg':'邮箱密码输入不正确'}
        return {'msg':'用户名不存在'}


class Modify(Resource):
    def post(self):
        data={
            'msg':'修改成功'
        }
        users=User.query.get(1)
        users.name='zs'
        db.session.add(users)
        db.session.commit()
        return jsonify(data)
class Del(Resource):
    def post(self):
        data={
            'msg':'删除成功'
        }
        users=User.query.get(1)
        db.session.delete(users)
        db.session.commit()
        return jsonify(data)









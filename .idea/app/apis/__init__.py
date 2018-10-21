
from flask_restful import Api

from app.apis.BlogApi import B_Register, B_Modify, B_Del
from app.apis.UserApi import Login, Modify, Del, Register

api = Api()

def init_apis(app):
    api.init_app(app=app)



api.add_resource(Register,'/register/')
api.add_resource(Login,'/login/')
api.add_resource(Modify,'/modify/')
api.add_resource(Del,'/delete/')
api.add_resource(B_Register,'/b_register/')
api.add_resource(B_Modify,'/b_modify/')
api.add_resource(B_Del,'/b_del/')

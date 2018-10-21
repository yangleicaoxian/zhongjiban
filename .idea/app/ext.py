from flask_migrate import Migrate


from app.models import db


migrate = Migrate()

def init_ext(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/Test'
    db.init_app(app=app)
    migrate.init_app(app=app,db=db)




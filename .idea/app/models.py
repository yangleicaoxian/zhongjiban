from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    email=db.Column(db.String(64))
    name=db.Column(db.String(32))
    password=db.Column(db.String(32))
    icon=db.Column(db.String(32))
    delete=db.Column(db.String(32))

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(32))
    email=db.Column(db.String(32))
    password=db.Column(db.String(32))
    telephone=db.Column(db.INTEGER)
    title=db.Column(db.String(256))
    content=db.Column(db.String(512))
class  Collect(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    c_user=db.Column(db.Integer,db.ForeignKey(User.id))
    c_blog=db.Column(db.Integer,db.ForeignKey(Blog.id))



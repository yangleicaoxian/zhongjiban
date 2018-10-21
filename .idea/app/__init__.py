from flask import Flask

from app.apis import init_apis
from app.ext import init_ext
from app.models import db


def create_app():
    app=Flask(__name__)
    db.init_app(app=app)
    init_ext(app)
    init_apis(app)

    return app
import os
import secrets

from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from db import db

from models import ItemModel
from models import StoreModel

from Resources.item import blp as ItemBlueprint
from Resources.store import blp as StoreBlueprint
from Resources.tag import blp as TagBlueprint


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "31329424013196456479488273901868198862" #secrets.SystemRandom().getrandbits(128)#"jose" not safe pass in bits
    jwt = JWTManager(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(StoreBlueprint)

    return app
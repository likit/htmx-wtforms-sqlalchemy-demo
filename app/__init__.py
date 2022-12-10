import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)  # create an instance of Flask app
    app.config.from_mapping(
            SECRET_KEY='supersecretkey',
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:',
            )
    db.init_app(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from app.main import main_blueprint

    app.register_blueprint(main_blueprint)

    return app


app = create_app()

from app.main.models import *

with app.app_context():
    db.create_all()

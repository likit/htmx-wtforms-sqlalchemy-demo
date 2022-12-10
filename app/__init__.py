import os
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)  # create an instance of Flask app
    app.config.from_mapping(
            SECRET_KEY='supersecretkey',
            SQLALCHEMY_DATABASE_URI='sqlite://:memory:'
            )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from app.main import main_blueprint

    app.register_blueprint(main_blueprint)

    return app


app = create_app()

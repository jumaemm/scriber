import os
from flask import Flask
from dotenv import load_dotenv
from flask import Blueprint
from scriber.extensions import db

load_dotenv()

def create_app(test_config=None):
    from . import api, site, auth
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_envvar('APP_CONFIG')
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    
    from scriber.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from scriber.site import bp as site_bp
    app.register_blueprint(site_bp)
    
    @app.route('/hello')
    def hello():
        return 'Hello there'
    
    return app
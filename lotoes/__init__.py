"""Flask application creation factory."""
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from config import config
from .blueprints import mount_blueprints

#db = SQLAlchemy()

def create_app(config_name, set_utf=True):
    """App creation factory based on the FLASK_CONFIG env var."""
    '''if set_utf:
        setdefaultencoding()'''
    app = Flask(__name__) 
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    #login_manager.init_app(app)

    mount_blueprints(app, config_name)

    return app
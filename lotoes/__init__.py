"""Flask application creation factory."""
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
from .blueprints import mount_blueprints
from .extensions import register_error_handlers

db = SQLAlchemy()

login_manager = LoginManager()

login_manager.session_protection = 'strong'
login_manager.login_view = 'usuarios.login'
#login_manager.login_message_category = 'info'

def setdefaultencoding():
    if sys.version[0] == '2':
        reload(sys)
        sys.setdefaultencoding('utf-8')

def create_app(config_name, set_utf=True):
    """App creation factory based on the FLASK_CONFIG env var."""
    if set_utf:
        setdefaultencoding()
    app = Flask(__name__) 
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    mount_blueprints(app, config_name)

    register_error_handlers(app)

    return app
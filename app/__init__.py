from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from .config import Config
from .auth import auth
from .welcome import greetings
from .modelsdb import db
from .models import UserModel

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)

def create_app():
    # Create a new instance of Flask
    app = Flask(__name__)

    # Initialize bootstrap
    bootstrap = Bootstrap(app=app)

    # Create a secret key with flask to use a session
    app.config.from_object(Config)

    # Insert the login manager
    login_manager.init_app(app)

    # We need to register the blueprint
    app.register_blueprint(auth)
    app.register_blueprint(greetings)

    # Connect with database
    db.init_app(app=app)

    return app
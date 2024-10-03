from flask import Flask
from flask_basicauth import BasicAuth
from .routes import configure_routes
from .config_loader import load_config
from .logger import logger


def create_app():
    app = Flask(__name__)

    # Load configuration
    config = load_config()

    # Set up Basic Authentication
    app.config['BASIC_AUTH_USERNAME'] = list(config['users'].keys())[0]
    app.config['BASIC_AUTH_PASSWORD'] = config['users'][app.config['BASIC_AUTH_USERNAME']]['password']
    basic_auth = BasicAuth(app)

    # Register routes
    configure_routes(app)

    logger.info("Application created and configured.")

    return app

from flask import Flask 
from db import db
from flask_restful import Api
from flask_migrate import Migrate
from flask_cors import CORS
import os
from mail import mail

from resources.check import CheckResource

api = Api()
migrate = Migrate()
cors = CORS()

api.add_resource(CheckResource, '/check')

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('FLASK_DATABASE_URL')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'apikey'
    app.config['MAIL_PASSWORD'] = os.environ.get('SENDGRID_API_KEY')
    app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')

    db.init_app(app)
    api.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    mail.init_app(app)

    @app.route('/')
    def helloWorld():
        return """
            Thank you so much for visiting. This is the api - visiting klaar.xyz for the web app.
        """

    return app

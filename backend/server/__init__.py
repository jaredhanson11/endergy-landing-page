'''
This package contains the Flask REST Api for the Endergy Landing Page.
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from . import routes

# Initiliaze Flask app object with configs

app = Flask(__name__)  # pylint: disable=invalid-name
app.config.from_envvar('APP_CONFIG')

# Initialize Flask-SQLAlchemy db object
db = SQLAlchemy(app)  # pylint: disable=invalid-name
# Initialize Flask-RESTful api object
api = Api(app)  # pylint: disable=invalid-name

# Attach routes to the Flask-RESTful Resource objects found at controllers/*
routes.add_routes(api)

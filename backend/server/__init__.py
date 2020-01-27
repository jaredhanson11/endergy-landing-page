'''
This package contains the Flask REST Api for the Endergy Landing Page.
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

# Initiliaze Flask app object with configs
app = Flask(__name__)
app.config.from_envvar('APP_CONFIG')

# Initialize Flask-SQLAlchemy db object
db = SQLAlchemy(app)
# Initialize Flask-RESTful api object
api = Api(app)

# Ugly dependency, but since routes import controller classes
# the api and app objects needs to be avaible on importing routes
from . import routes
# Attach routes to the Flask-RESTful Resource objects found at controllers/*
routes.add_routes(api)

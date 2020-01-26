'''
Config object, relies heavily on environment variables being set.
'''
import os

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = os.environ.get('SQL_CONNECTION_URI')

# Flask Mail
MAIL_SERVER = 'smtp@gmail.com'
MAIL_PORT = 587
MAIL_USE_SSL = True,
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

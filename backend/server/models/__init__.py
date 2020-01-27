'''
Module contians database models which are SQLAlchemy objects.
'''
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    '''
    BaseModel that all SQL models should inherit from.
    Forces table to be created in specific schema.

    Although this complexity really isn't required, I'm keeping the use of a
    separate schema for reference in more important projects.
    '''
    __table_args__ = {"schema": "endergy_landing_page"}

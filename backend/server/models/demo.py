'''
Visitors to Endergy landing page can request a demo of the product. DemoModel
is an object that represents the demo request.
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DemoModel(Base):  # pylint: disable=too-few-public-methods
    '''
    DemoModel stores requests for more info on Endergy made by potential
    customers on the landing page.
    '''

    __tablename__ = 'demo'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), required=True)
    email = Column(String(120))
    phone = Column(String(20))
    use_case = Column(String(20))
    use_case_description = Column(String(2000))

    def __init__(self, name=None, email=None, phone=None, use_case=None,
                 use_case_desc=None):  # pylint: disable=too-many-arguments
        self.name = name
        self.email = email
        self.phone = phone
        self.use_case = use_case
        self.use_case_description = use_case_desc

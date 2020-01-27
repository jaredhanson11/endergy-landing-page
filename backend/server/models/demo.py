'''
Visitors to Endergy landing page can request a demo of the product. DemoModel
is an object that represents the demo request.
'''

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from . import Base, BaseModel
from ..objects.demo_request import DemoRequest


class DemoModel(Base, BaseModel):
    '''
    DemoModel stores requests for more info on Endergy made by potential
    customers on the landing page.
    '''

    __tablename__ = 'demo'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120))
    phone = Column(String(20))
    use_case = Column(String(20))
    use_case_description = Column(String(2000))
    created_date = Column(DateTime, default=datetime.utcnow)

    def __init__(self, demo_request: DemoRequest):
        self.name = demo_request.name
        self.email = demo_request.email
        self.phone = demo_request.phone
        self.use_case = demo_request.use_case
        self.use_case_description = demo_request.use_case_description

'''
Controller receiving demo requests from potential customers.
'''

from flask import request
from flask_restful import Resource

from endergy_email.email_client import GmailClient

from . import db
from . import app
from ..models.demo import DemoModel
from ..objects.demo_request import DemoRequest

from ..utils import responses


class DemoController(Resource):
    '''
    Handles requests by customers surrounding Endergy demo's.
    '''
    gmail_client = GmailClient(app.config.get('MAIL_USERNAME'),
                               app.config.get('MAIL_PASSWORD'))

    def post(self):
        '''
        Creates Demo record and saves to database.
        '''
        post_data = request.get_json(force=True, silent=False)
        demo_request = DemoRequest(post_data)
        demo_record = DemoModel(demo_request)
        db.session.add(demo_record)
        db.session.commit()
        DemoController.gmail_client.send_gmail(
            'jred0011@gmail.com', str(post_data), 'New Demo Request')
        return responses.success(None)

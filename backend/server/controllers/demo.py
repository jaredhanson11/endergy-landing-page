'''
Controller receiving demo requests from potential customers.
'''

from flask import request
from flask_restful import Resource

from . import db
from ..models.demo import DemoModel
from ..objects.demo_request import DemoRequest

from ..utils import responses


class DemoController(Resource):
    '''
    Handles requests by customers surrounding Endergy demo's.
    '''

    def post(self):
        '''
        Creates Demo record and saves to database.
        '''
        post_data = request.get_json(force=True, silent=False)
        demo_request = DemoRequest(post_data)
        demo_record = DemoModel(demo_request)
        db.session.add(demo_record)
        db.session.commit()
        return responses.success(None)

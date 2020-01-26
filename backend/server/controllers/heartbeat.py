'''
Controllers surrounding heartbeat of the server.
'''
from time import time
from flask_restful import Resource

from ..utils import responses


class HeartbeatController(Resource):
    '''
    Controller with server's heartbeat.
    '''
    def get(self):  # pylint: disable=no-self-use
        '''
        Returns current time.
        '''
        ret = {'timenow': int(time())}
        return responses.success(ret, 200)

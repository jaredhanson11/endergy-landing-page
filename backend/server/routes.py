'''
Setup all the api routes in add_routes(api) method.
'''
from .controllers import heartbeat


def add_routes(api):
    '''
    Sets up all the api routes.
    '''
    api.add_resource(heartbeat.HeartbeatController, '/hb')

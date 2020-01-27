'''
Contains BaseRequest class
'''


class BaseRequest:
    '''
    Base class for request object. Allows for initialization of fields for
    that object using a dictionary to map to the fields.
    '''
    def __init__(self, fields: dict):
        self.__dict__.update(fields)

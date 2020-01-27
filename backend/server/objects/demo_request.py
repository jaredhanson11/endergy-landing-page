'''
Common constants related to the Demo request flows.
'''
from .base_request import BaseRequest


class DemoRequest(BaseRequest):
    '''
    Constants and fields related to the DemoRequest flow.
    '''
    name = None
    email = None
    phone = None
    use_case = None
    use_case_description = None

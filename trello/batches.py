# TODO: is this needed for our System

from .api_client import APIClient

REFERENCE_TARGET = 'batch'


class Batch:

    def __init__(self, apikey, token):
        self._api_client = APIClient(apikey, token)

    ### Get Section ###

    ### Post Section ###

    ### Put Section ###

    ### Delete Section ###


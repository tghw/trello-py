# Copy and Paste Setup for making new classes in .py files

from .api_client import APIClient

REFERENCE_TARGET = 'name in url'


class Name: # name of the REST API sectoin

    def __init__(self, apikey, token):
        self._api_client = APIClient(apikey, token)

    ### Get Section ###

    ### Post Section ###

    ### Put Section ###

    ### Delete Section ###
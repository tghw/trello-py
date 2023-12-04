from .api_client import APIClient

REFERENCE_TARGET = 'search'


class Search:

    def __init__(self, apikey, token):
        self._api_client = APIClient(apikey, token)

    ### Get Section ###

    def search(self, query: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, required_target_id=False, query=query, **kwargs)

    def search_members(self, query: str, board_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, target_id='members', idBoard=board_id, query=query, **kwargs)

    ### Post Section ###

    ### Put Section ###

    ### Delete Section ###

from .base import ApiBase
import requests

class Types(ApiBase):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, team_or_user_id):
        resp = requests.get(f"https://trello.com/1/types/{team_or_user_id}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)


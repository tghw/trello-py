from .base import ApiBase
import requests

class Batches(ApiBase):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, urls):
        resp = requests.get("https://trello.com/1/batch", params={"key": self._apikey, "token": self._token, "urls": urls}, data=None)
        return self.raise_or_json(resp)


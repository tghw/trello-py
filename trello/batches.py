import json
import requests

class Batches(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, urls):
        resp = requests.get("https://trello.com/1/batch".format(), params={"key": self._apikey, "token": self._token, "urls": urls}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)


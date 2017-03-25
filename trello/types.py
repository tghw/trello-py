import json
import requests

class Types(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, team_or_user_id):
        resp = requests.get("https://trello.com/1/types/{}".format(team_or_user_id), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)


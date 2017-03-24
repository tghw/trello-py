import json
import requests

class Labels(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idLabel, fields=None):
        resp = requests.get("https://trello.com/1/labels/%s" % (idLabel), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board(self, idLabel, fields=None):
        resp = requests.get("https://trello.com/1/labels/%s/board" % (idLabel), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board_field(self, field, idLabel):
        resp = requests.get("https://trello.com/1/labels/%s/board/%s" % (idLabel, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def update(self, idLabel, name=None, color=None):
        resp = requests.put("https://trello.com/1/labels/%s" % (idLabel), params=dict(key=self._apikey, token=self._token), data=dict(name=name, color=color))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_color(self, idLabel, value):
        resp = requests.put("https://trello.com/1/labels/%s/color" % (idLabel), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_name(self, idLabel, value):
        resp = requests.put("https://trello.com/1/labels/%s/name" % (idLabel), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new(self, name, color, idBoard):
        resp = requests.post("https://trello.com/1/labels" % (), params=dict(key=self._apikey, token=self._token), data=dict(name=name, color=color, idBoard=idBoard))
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete(self, idLabel):
        resp = requests.delete("https://trello.com/1/labels/%s" % (idLabel), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)


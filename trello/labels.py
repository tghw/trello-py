import json
import requests

class Labels(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idLabel, fields=None):
        resp = requests.get("https://trello.com/1/labels/{}".format(idLabel), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_board(self, idLabel, fields=None):
        resp = requests.get("https://trello.com/1/labels/{}/board".format(idLabel), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_board_field(self, field, idLabel):
        resp = requests.get("https://trello.com/1/labels/{}/board/{}".format(idLabel, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def update(self, idLabel, name=None, color=None):
        resp = requests.put("https://trello.com/1/labels/{}".format(idLabel), params={"key": self._apikey, "token": self._token}, data={"name": name, "color": color})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_color(self, idLabel, value):
        resp = requests.put("https://trello.com/1/labels/{}/color".format(idLabel), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_name(self, idLabel, value):
        resp = requests.put("https://trello.com/1/labels/{}/name".format(idLabel), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def new(self, name, color, idBoard):
        resp = requests.post("https://trello.com/1/labels".format(), params={"key": self._apikey, "token": self._token}, data={"name": name, "color": color, "idBoard": idBoard})
        resp.raise_for_status()
        return json.loads(resp.text)

    def delete(self, idLabel):
        resp = requests.delete("https://trello.com/1/labels/{}".format(idLabel), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)


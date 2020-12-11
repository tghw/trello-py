from .base import ApiBase
import requests

class Labels(ApiBase):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idLabel, fields=None):
        resp = requests.get(f"https://trello.com/1/labels/{idLabel}", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_board(self, idLabel, fields=None):
        resp = requests.get(f"https://trello.com/1/labels/{idLabel}/board", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_board_field(self, field, idLabel):
        resp = requests.get(f"https://trello.com/1/labels/{idLabel}/board/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def update(self, idLabel, name=None, color=None):
        resp = requests.put(f"https://trello.com/1/labels/{idLabel}", params={"key": self._apikey, "token": self._token}, data={"name": name, "color": color})
        return self.raise_or_json(resp)

    def update_color(self, idLabel, value):
        resp = requests.put(f"https://trello.com/1/labels/{idLabel}/color", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_name(self, idLabel, value):
        resp = requests.put(f"https://trello.com/1/labels/{idLabel}/name", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def new(self, name, color, idBoard):
        resp = requests.post("https://trello.com/1/labels", params={"key": self._apikey, "token": self._token}, data={"name": name, "color": color, "idBoard": idBoard})
        return self.raise_or_json(resp)

    def delete(self, idLabel):
        resp = requests.delete(f"https://trello.com/1/labels/{idLabel}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)


import json
import requests

class Webhooks(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get_(self, idWebhook):
        resp = requests.get("https://trello.com/1/webhooks/{}/".format(idWebhook), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_field(self, field, idWebhook):
        resp = requests.get("https://trello.com/1/webhooks/{}/{}".format(idWebhook, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def update(self, idWebhook, description=None, callbackURL=None, idModel=None, active=None):
        resp = requests.put("https://trello.com/1/webhooks/{}".format(idWebhook), params={"key": self._apikey, "token": self._token}, data={"description": description, "callbackURL": callbackURL, "idModel": idModel, "active": active})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_(self, callbackURL, idModel, description=None):
        resp = requests.put("https://trello.com/1/webhooks/".format(), params={"key": self._apikey, "token": self._token}, data={"callbackURL": callbackURL, "idModel": idModel, "description": description})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_active(self, idWebhook, value):
        resp = requests.put("https://trello.com/1/webhooks/{}/active".format(idWebhook), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_callbackURL(self, idWebhook, value):
        resp = requests.put("https://trello.com/1/webhooks/{}/callbackURL".format(idWebhook), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_description(self, idWebhook, value):
        resp = requests.put("https://trello.com/1/webhooks/{}/description".format(idWebhook), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_idModel(self, idWebhook, value):
        resp = requests.put("https://trello.com/1/webhooks/{}/idModel".format(idWebhook), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def new(self, callbackURL, idModel, description=None):
        resp = requests.post("https://trello.com/1/webhooks".format(), params={"key": self._apikey, "token": self._token}, data={"callbackURL": callbackURL, "idModel": idModel, "description": description})
        resp.raise_for_status()
        return json.loads(resp.text)

    def delete(self, idWebhook):
        resp = requests.delete("https://trello.com/1/webhooks/{}".format(idWebhook), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)


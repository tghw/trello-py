import json
import requests

class Tokens(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, token, fields=None, webhooks=None):
        resp = requests.get("https://trello.com/1/tokens/{}".format(token), params={"key": self._apikey, "token": self._token, "fields": fields, "webhooks": webhooks}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_field(self, field, token):
        resp = requests.get("https://trello.com/1/tokens/{}/{}".format(token, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_member(self, token, fields=None):
        resp = requests.get("https://trello.com/1/tokens/{}/member".format(token), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_member_field(self, field, token):
        resp = requests.get("https://trello.com/1/tokens/{}/member/{}".format(token, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_webhook(self, token):
        resp = requests.get("https://trello.com/1/tokens/{}/webhooks".format(token), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_webhook_idWebhook(self, idWebhook, token):
        resp = requests.get("https://trello.com/1/tokens/{}/webhooks/{}".format(token, idWebhook), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_webhook(self, token, callbackURL, idModel, description=None):
        resp = requests.put("https://trello.com/1/tokens/{}/webhooks".format(token), params={"key": self._apikey, "token": self._token}, data={"callbackURL": callbackURL, "idModel": idModel, "description": description})
        resp.raise_for_status()
        return json.loads(resp.text)

    def new_webhook(self, token, callbackURL, idModel, description=None):
        resp = requests.post("https://trello.com/1/tokens/{}/webhooks".format(token), params={"key": self._apikey, "token": self._token}, data={"callbackURL": callbackURL, "idModel": idModel, "description": description})
        resp.raise_for_status()
        return json.loads(resp.text)

    def delete(self, token):
        resp = requests.delete("https://trello.com/1/tokens/{}".format(token), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def delete_webhook_idWebhook(self, idWebhook, token):
        resp = requests.delete("https://trello.com/1/tokens/{}/webhooks/{}".format(token, idWebhook), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)


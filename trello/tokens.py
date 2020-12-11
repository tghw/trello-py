from .base import ApiBase
import requests

class Tokens(ApiBase):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, token, fields=None, webhooks=None):
        resp = requests.get(f"https://trello.com/1/tokens/{token}", params={"key": self._apikey, "token": self._token, "fields": fields, "webhooks": webhooks}, data=None)
        return self.raise_or_json(resp)

    def get_field(self, field, token):
        resp = requests.get(f"https://trello.com/1/tokens/{token}/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_member(self, token, fields=None):
        resp = requests.get(f"https://trello.com/1/tokens/{token}/member", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_member_field(self, field, token):
        resp = requests.get(f"https://trello.com/1/tokens/{token}/member/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_webhook(self, token):
        resp = requests.get(f"https://trello.com/1/tokens/{token}/webhooks", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_webhook_idWebhook(self, idWebhook, token):
        resp = requests.get(f"https://trello.com/1/tokens/{token}/webhooks/{idWebhook}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def update_webhook(self, token, callbackURL, idModel, description=None):
        resp = requests.put(f"https://trello.com/1/tokens/{token}/webhooks", params={"key": self._apikey, "token": self._token}, data={"callbackURL": callbackURL, "idModel": idModel, "description": description})
        return self.raise_or_json(resp)

    def new_webhook(self, token, callbackURL, idModel, description=None):
        resp = requests.post(f"https://trello.com/1/tokens/{token}/webhooks", params={"key": self._apikey, "token": self._token}, data={"callbackURL": callbackURL, "idModel": idModel, "description": description})
        return self.raise_or_json(resp)

    def delete(self, token):
        resp = requests.delete(f"https://trello.com/1/tokens/{token}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def delete_webhook_idWebhook(self, idWebhook, token):
        resp = requests.delete(f"https://trello.com/1/tokens/{token}/webhooks/{idWebhook}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)


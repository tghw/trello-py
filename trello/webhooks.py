from .base import ApiBase
import warnings
import requests

class Webhooks(ApiBase):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get_(self, idWebhook):
        warnings.warn('.get_() is deprecated. Please use .get()', DeprecationWarning)
        return self.get(idWebhook)

    def get(self, idWebhook):
        resp = requests.get(f"https://trello.com/1/webhooks/{idWebhook}/", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_field(self, field, idWebhook):
        resp = requests.get(f"https://trello.com/1/webhooks/{idWebhook}/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def update(self, idWebhook, description=None, callbackURL=None, idModel=None, active=None):
        resp = requests.put(f"https://trello.com/1/webhooks/{idWebhook}", params={"key": self._apikey, "token": self._token}, data={"description": description, "callbackURL": callbackURL, "idModel": idModel, "active": active})
        return self.raise_or_json(resp)

    def update_(self, callbackURL, idModel, description=None):
        warnings.warn('.update_() is deprecated. Please use .update()', DeprecationWarning)
        return self.update(callbackURL, idModel, description)

    def update_active(self, idWebhook, value):
        resp = requests.put(f"https://trello.com/1/webhooks/{idWebhook}/active", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_callbackURL(self, idWebhook, value):
        resp = requests.put(f"https://trello.com/1/webhooks/{idWebhook}/callbackURL", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_description(self, idWebhook, value):
        resp = requests.put(f"https://trello.com/1/webhooks/{idWebhook}/description", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_idModel(self, idWebhook, value):
        resp = requests.put(f"https://trello.com/1/webhooks/{idWebhook}/idModel", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def new(self, callbackURL, idModel, description=None):
        resp = requests.post("https://trello.com/1/webhooks", params={"key": self._apikey, "token": self._token}, data={"callbackURL": callbackURL, "idModel": idModel, "description": description})
        return self.raise_or_json(resp)

    def delete(self, idWebhook):
        resp = requests.delete(f"https://trello.com/1/webhooks/{idWebhook}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)


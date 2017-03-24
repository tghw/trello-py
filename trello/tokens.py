import json
import requests

class Tokens(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, token, fields=None, webhooks=None):
        resp = requests.get("https://trello.com/1/tokens/%s" % (token), params=dict(key=self._apikey, token=self._token, fields=fields, webhooks=webhooks), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_field(self, field, token):
        resp = requests.get("https://trello.com/1/tokens/%s/%s" % (token, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member(self, token, fields=None):
        resp = requests.get("https://trello.com/1/tokens/%s/member" % (token), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member_field(self, field, token):
        resp = requests.get("https://trello.com/1/tokens/%s/member/%s" % (token, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_webhook(self, token):
        resp = requests.get("https://trello.com/1/tokens/%s/webhooks" % (token), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_webhook_idWebhook(self, idWebhook, token):
        resp = requests.get("https://trello.com/1/tokens/%s/webhooks/%s" % (token, idWebhook), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_webhook(self, token, callbackURL, idModel, description=None):
        resp = requests.put("https://trello.com/1/tokens/%s/webhooks" % (token), params=dict(key=self._apikey, token=self._token), data=dict(callbackURL=callbackURL, idModel=idModel, description=description))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_webhook(self, token, callbackURL, idModel, description=None):
        resp = requests.post("https://trello.com/1/tokens/%s/webhooks" % (token), params=dict(key=self._apikey, token=self._token), data=dict(callbackURL=callbackURL, idModel=idModel, description=description))
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete(self, token):
        resp = requests.delete("https://trello.com/1/tokens/%s" % (token), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete_webhook_idWebhook(self, idWebhook, token):
        resp = requests.delete("https://trello.com/1/tokens/%s/webhooks/%s" % (token, idWebhook), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)


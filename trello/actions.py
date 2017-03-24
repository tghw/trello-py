import json
import requests

class Actions(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idAction, display=None, entities=None, fields=None, member=None, member_fields=None, memberCreator=None, memberCreator_fields=None):
        resp = requests.get("https://trello.com/1/actions/%s" % (idAction), params=dict(key=self._apikey, token=self._token, display=display, entities=entities, fields=fields, member=member, member_fields=member_fields, memberCreator=memberCreator, memberCreator_fields=memberCreator_fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_field(self, field, idAction):
        resp = requests.get("https://trello.com/1/actions/%s/%s" % (idAction, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board(self, idAction, fields=None):
        resp = requests.get("https://trello.com/1/actions/%s/board" % (idAction), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board_field(self, field, idAction):
        resp = requests.get("https://trello.com/1/actions/%s/board/%s" % (idAction, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card(self, idAction, fields=None):
        resp = requests.get("https://trello.com/1/actions/%s/card" % (idAction), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card_field(self, field, idAction):
        resp = requests.get("https://trello.com/1/actions/%s/card/%s" % (idAction, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_display(self, idAction):
        resp = requests.get("https://trello.com/1/actions/%s/display" % (idAction), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_entitie(self, idAction):
        resp = requests.get("https://trello.com/1/actions/%s/entities" % (idAction), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_list(self, idAction, fields=None):
        resp = requests.get("https://trello.com/1/actions/%s/list" % (idAction), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_list_field(self, field, idAction):
        resp = requests.get("https://trello.com/1/actions/%s/list/%s" % (idAction, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member(self, idAction, fields=None):
        resp = requests.get("https://trello.com/1/actions/%s/member" % (idAction), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member_field(self, field, idAction):
        resp = requests.get("https://trello.com/1/actions/%s/member/%s" % (idAction, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_memberCreator(self, idAction, fields=None):
        resp = requests.get("https://trello.com/1/actions/%s/memberCreator" % (idAction), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_memberCreator_field(self, field, idAction):
        resp = requests.get("https://trello.com/1/actions/%s/memberCreator/%s" % (idAction, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_organization(self, idAction, fields=None):
        resp = requests.get("https://trello.com/1/actions/%s/organization" % (idAction), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_organization_field(self, field, idAction):
        resp = requests.get("https://trello.com/1/actions/%s/organization/%s" % (idAction, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def update(self, idAction, text=None):
        resp = requests.put("https://trello.com/1/actions/%s" % (idAction), params=dict(key=self._apikey, token=self._token), data=dict(text=text))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_text(self, idAction, value):
        resp = requests.put("https://trello.com/1/actions/%s/text" % (idAction), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete(self, idAction):
        resp = requests.delete("https://trello.com/1/actions/%s" % (idAction), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)


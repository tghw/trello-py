import json
import requests

class Checklists(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, checklist_id, cards=None, card_fields=None, checkItems=None, checkItem_fields=None, fields=None):
        resp = requests.get("https://trello.com/1/checklists/%s" % (checklist_id), params=dict(key=self._apikey, token=self._token, cards=cards, card_fields=card_fields, checkItems=checkItems, checkItem_fields=checkItem_fields, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_field(self, field, checklist_id):
        resp = requests.get("https://trello.com/1/checklists/%s/%s" % (checklist_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board(self, checklist_id, fields=None):
        resp = requests.get("https://trello.com/1/checklists/%s/board" % (checklist_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board_field(self, field, checklist_id):
        resp = requests.get("https://trello.com/1/checklists/%s/board/%s" % (checklist_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card(self, checklist_id, actions=None, attachments=None, members=None, checkItemStates=None, checklists=None, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/checklists/%s/cards" % (checklist_id), params=dict(key=self._apikey, token=self._token, actions=actions, attachments=attachments, members=members, checkItemStates=checkItemStates, checklists=checklists, filter=filter, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card_filter(self, filter, checklist_id):
        resp = requests.get("https://trello.com/1/checklists/%s/cards/%s" % (checklist_id, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_checkItem(self, checklist_id, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/checklists/%s/checkItems" % (checklist_id), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def update(self, checklist_id, name=None):
        resp = requests.put("https://trello.com/1/checklists/%s" % (checklist_id), params=dict(key=self._apikey, token=self._token), data=dict(name=name))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_name(self, checklist_id, value):
        resp = requests.put("https://trello.com/1/checklists/%s/name" % (checklist_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new(self, name, idBoard):
        resp = requests.post("https://trello.com/1/checklists" % (), params=dict(key=self._apikey, token=self._token), data=dict(name=name, idBoard=idBoard))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_checkItem(self, checklist_id, name):
        resp = requests.post("https://trello.com/1/checklists/%s/checkItems" % (checklist_id), params=dict(key=self._apikey, token=self._token), data=dict(name=name))
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete_checkItem_idCheckItem(self, idCheckItem, checklist_id):
        resp = requests.delete("https://trello.com/1/checklists/%s/checkItems/%s" % (checklist_id, idCheckItem), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    

import json
import requests

class Lists(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idList, cards=None, card_fields=None, fields=None):
        resp = requests.get("https://trello.com/1/lists/%s" % (idList), params=dict(key=self._apikey, token=self._token, cards=cards, card_fields=card_fields, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_field(self, field, idList):
        resp = requests.get("https://trello.com/1/lists/%s/%s" % (idList, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_action(self, idList, entities=None, filter=None, fields=None, limit=None, format=None, since=None, page=None, idModels=None):
        resp = requests.get("https://trello.com/1/lists/%s/actions" % (idList), params=dict(key=self._apikey, token=self._token, entities=entities, filter=filter, fields=fields, limit=limit, format=format, since=since, page=page, idModels=idModels), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board(self, idList, fields=None):
        resp = requests.get("https://trello.com/1/lists/%s/board" % (idList), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board_field(self, field, idList):
        resp = requests.get("https://trello.com/1/lists/%s/board/%s" % (idList, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card(self, idList, actions=None, attachments=None, attachment_fields=None, members=None, member_fields=None, checkItemStates=None, checklists=None, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/lists/%s/cards" % (idList), params=dict(key=self._apikey, token=self._token, actions=actions, attachments=attachments, attachment_fields=attachment_fields, members=members, member_fields=member_fields, checkItemStates=checkItemStates, checklists=checklists, filter=filter, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card_filter(self, filter, idList):
        resp = requests.get("https://trello.com/1/lists/%s/cards/%s" % (idList, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def update(self, idList, name=None, closed=None, idBoard=None, pos=None, subscribed=None):
        resp = requests.put("https://trello.com/1/lists/%s" % (idList), params=dict(key=self._apikey, token=self._token), data=dict(name=name, closed=closed, idBoard=idBoard, pos=pos, subscribed=subscribed))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_closed(self, idList, value):
        resp = requests.put("https://trello.com/1/lists/%s/closed" % (idList), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_idBoard(self, idList, value, pos=None):
        resp = requests.put("https://trello.com/1/lists/%s/idBoard" % (idList), params=dict(key=self._apikey, token=self._token), data=dict(value=value, pos=pos))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_name(self, idList, value):
        resp = requests.put("https://trello.com/1/lists/%s/name" % (idList), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_po(self, idList, value):
        resp = requests.put("https://trello.com/1/lists/%s/pos" % (idList), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_subscribed(self, idList, value):
        resp = requests.put("https://trello.com/1/lists/%s/subscribed" % (idList), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new(self, name, idBoard, idListSource=None, pos=None):
        resp = requests.post("https://trello.com/1/lists" % (), params=dict(key=self._apikey, token=self._token), data=dict(name=name, idBoard=idBoard, idListSource=idListSource, pos=pos))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_card(self, idList, name, desc=None):
        resp = requests.post("https://trello.com/1/lists/%s/cards" % (idList), params=dict(key=self._apikey, token=self._token), data=dict(name=name, desc=desc))
        resp.raise_for_status()
        return json.loads(resp.content)


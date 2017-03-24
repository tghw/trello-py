import json
import requests

class Notifications(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idNotification, display=None, entities=None, fields=None, memberCreator=None, memberCreator_fields=None, board=None, board_fields=None, list=None, card=None, card_fields=None, organization=None, organization_fields=None, member=None, member_fields=None):
        resp = requests.get("https://trello.com/1/notifications/%s" % (idNotification), params=dict(key=self._apikey, token=self._token, display=display, entities=entities, fields=fields, memberCreator=memberCreator, memberCreator_fields=memberCreator_fields, board=board, board_fields=board_fields, list=list, card=card, card_fields=card_fields, organization=organization, organization_fields=organization_fields, member=member, member_fields=member_fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_field(self, field, idNotification):
        resp = requests.get("https://trello.com/1/notifications/%s/%s" % (idNotification, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board(self, idNotification, fields=None):
        resp = requests.get("https://trello.com/1/notifications/%s/board" % (idNotification), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board_field(self, field, idNotification):
        resp = requests.get("https://trello.com/1/notifications/%s/board/%s" % (idNotification, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card(self, idNotification, fields=None):
        resp = requests.get("https://trello.com/1/notifications/%s/card" % (idNotification), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card_field(self, field, idNotification):
        resp = requests.get("https://trello.com/1/notifications/%s/card/%s" % (idNotification, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_display(self, idNotification):
        resp = requests.get("https://trello.com/1/notifications/%s/display" % (idNotification), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_entitie(self, idNotification):
        resp = requests.get("https://trello.com/1/notifications/%s/entities" % (idNotification), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_list(self, idNotification, fields=None):
        resp = requests.get("https://trello.com/1/notifications/%s/list" % (idNotification), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_list_field(self, field, idNotification):
        resp = requests.get("https://trello.com/1/notifications/%s/list/%s" % (idNotification, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member(self, idNotification, fields=None):
        resp = requests.get("https://trello.com/1/notifications/%s/member" % (idNotification), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member_field(self, field, idNotification):
        resp = requests.get("https://trello.com/1/notifications/%s/member/%s" % (idNotification, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_memberCreator(self, idNotification, fields=None):
        resp = requests.get("https://trello.com/1/notifications/%s/memberCreator" % (idNotification), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_memberCreator_field(self, field, idNotification):
        resp = requests.get("https://trello.com/1/notifications/%s/memberCreator/%s" % (idNotification, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_organization(self, idNotification, fields=None):
        resp = requests.get("https://trello.com/1/notifications/%s/organization" % (idNotification), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_organization_field(self, field, idNotification):
        resp = requests.get("https://trello.com/1/notifications/%s/organization/%s" % (idNotification, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def update(self, idNotification, unread=None):
        resp = requests.put("https://trello.com/1/notifications/%s" % (idNotification), params=dict(key=self._apikey, token=self._token), data=dict(unread=unread))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_unread(self, idNotification, value):
        resp = requests.put("https://trello.com/1/notifications/%s/unread" % (idNotification), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_all_read(self, ):
        resp = requests.post("https://trello.com/1/notifications/all/read" % (), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)


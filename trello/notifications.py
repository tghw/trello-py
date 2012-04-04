import json
import requests

class Notifications(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, notification_id, fields=None, memberCreator=None, memberCreator_fields=None, board=None, board_fields=None, list=None, card=None, card_fields=None, organization=None, organization_fields=None, member=None, member_fields=None):
        resp = requests.get("https://trello.com/1/notifications/%s" % (notification_id), params=dict(key=self._apikey, token=self._token, fields=fields, memberCreator=memberCreator, memberCreator_fields=memberCreator_fields, board=board, board_fields=board_fields, list=list, card=card, card_fields=card_fields, organization=organization, organization_fields=organization_fields, member=member, member_fields=member_fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_field(self, field, notification_id):
        resp = requests.get("https://trello.com/1/notifications/%s/%s" % (notification_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board(self, notification_id, fields=None):
        resp = requests.get("https://trello.com/1/notifications/%s/board" % (notification_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board_field(self, field, notification_id):
        resp = requests.get("https://trello.com/1/notifications/%s/board/%s" % (notification_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card(self, notification_id, fields=None):
        resp = requests.get("https://trello.com/1/notifications/%s/card" % (notification_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card_field(self, field, notification_id):
        resp = requests.get("https://trello.com/1/notifications/%s/card/%s" % (notification_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_list(self, notification_id, fields=None):
        resp = requests.get("https://trello.com/1/notifications/%s/list" % (notification_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_list_field(self, field, notification_id):
        resp = requests.get("https://trello.com/1/notifications/%s/list/%s" % (notification_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member(self, notification_id, fields=None):
        resp = requests.get("https://trello.com/1/notifications/%s/member" % (notification_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member_field(self, field, notification_id):
        resp = requests.get("https://trello.com/1/notifications/%s/member/%s" % (notification_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_memberCreator(self, notification_id, fields=None):
        resp = requests.get("https://trello.com/1/notifications/%s/memberCreator" % (notification_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_memberCreator_field(self, field, notification_id):
        resp = requests.get("https://trello.com/1/notifications/%s/memberCreator/%s" % (notification_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_organization(self, notification_id, fields=None):
        resp = requests.get("https://trello.com/1/notifications/%s/organization" % (notification_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_organization_field(self, field, notification_id):
        resp = requests.get("https://trello.com/1/notifications/%s/organization/%s" % (notification_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    

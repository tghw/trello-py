import json
import requests

class Notifications(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idNotification, display=None, entities=None, fields=None, memberCreator=None, memberCreator_fields=None, board=None, board_fields=None, list=None, card=None, card_fields=None, organization=None, organization_fields=None, member=None, member_fields=None):
        resp = requests.get("https://trello.com/1/notifications/{}".format(idNotification), params={"key": self._apikey, "token": self._token, "display": display, "entities": entities, "fields": fields, "memberCreator": memberCreator, "memberCreator_fields": memberCreator_fields, "board": board, "board_fields": board_fields, "list": list, "card": card, "card_fields": card_fields, "organization": organization, "organization_fields": organization_fields, "member": member, "member_fields": member_fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_field(self, field, idNotification):
        resp = requests.get("https://trello.com/1/notifications/{}/{}".format(idNotification, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_board(self, idNotification, fields=None):
        resp = requests.get("https://trello.com/1/notifications/{}/board".format(idNotification), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_board_field(self, field, idNotification):
        resp = requests.get("https://trello.com/1/notifications/{}/board/{}".format(idNotification, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_card(self, idNotification, fields=None):
        resp = requests.get("https://trello.com/1/notifications/{}/card".format(idNotification), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_card_field(self, field, idNotification):
        resp = requests.get("https://trello.com/1/notifications/{}/card/{}".format(idNotification, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_display(self, idNotification):
        resp = requests.get("https://trello.com/1/notifications/{}/display".format(idNotification), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_entitie(self, idNotification):
        resp = requests.get("https://trello.com/1/notifications/{}/entities".format(idNotification), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_list(self, idNotification, fields=None):
        resp = requests.get("https://trello.com/1/notifications/{}/list".format(idNotification), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_list_field(self, field, idNotification):
        resp = requests.get("https://trello.com/1/notifications/{}/list/{}".format(idNotification, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_member(self, idNotification, fields=None):
        resp = requests.get("https://trello.com/1/notifications/{}/member".format(idNotification), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_member_field(self, field, idNotification):
        resp = requests.get("https://trello.com/1/notifications/{}/member/{}".format(idNotification, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_memberCreator(self, idNotification, fields=None):
        resp = requests.get("https://trello.com/1/notifications/{}/memberCreator".format(idNotification), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_memberCreator_field(self, field, idNotification):
        resp = requests.get("https://trello.com/1/notifications/{}/memberCreator/{}".format(idNotification, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_organization(self, idNotification, fields=None):
        resp = requests.get("https://trello.com/1/notifications/{}/organization".format(idNotification), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_organization_field(self, field, idNotification):
        resp = requests.get("https://trello.com/1/notifications/{}/organization/{}".format(idNotification, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def update(self, idNotification, unread=None):
        resp = requests.put("https://trello.com/1/notifications/{}".format(idNotification), params={"key": self._apikey, "token": self._token}, data={"unread": unread})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_unread(self, idNotification, value):
        resp = requests.put("https://trello.com/1/notifications/{}/unread".format(idNotification), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def new_all_read(self, ):
        resp = requests.post("https://trello.com/1/notifications/all/read".format(), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)


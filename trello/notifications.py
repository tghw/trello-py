from .base import ApiBase
import requests

class Notifications(ApiBase):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idNotification, display=None, entities=None, fields=None, memberCreator=None, memberCreator_fields=None, board=None, board_fields=None, list=None, card=None, card_fields=None, organization=None, organization_fields=None, member=None, member_fields=None):
        resp = requests.get(f"https://trello.com/1/notifications/{idNotification}", params={"key": self._apikey, "token": self._token, "display": display, "entities": entities, "fields": fields, "memberCreator": memberCreator, "memberCreator_fields": memberCreator_fields, "board": board, "board_fields": board_fields, "list": list, "card": card, "card_fields": card_fields, "organization": organization, "organization_fields": organization_fields, "member": member, "member_fields": member_fields}, data=None)
        return self.raise_or_json(resp)

    def get_field(self, field, idNotification):
        resp = requests.get(f"https://trello.com/1/notifications/{idNotification}/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_board(self, idNotification, fields=None):
        resp = requests.get(f"https://trello.com/1/notifications/{idNotification}/board", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_board_field(self, field, idNotification):
        resp = requests.get(f"https://trello.com/1/notifications/{idNotification}/board/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_card(self, idNotification, fields=None):
        resp = requests.get(f"https://trello.com/1/notifications/{idNotification}/card", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_card_field(self, field, idNotification):
        resp = requests.get(f"https://trello.com/1/notifications/{idNotification}/card/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_display(self, idNotification):
        resp = requests.get(f"https://trello.com/1/notifications/{idNotification}/display", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_entitie(self, idNotification):
        resp = requests.get(f"https://trello.com/1/notifications/{idNotification}/entities", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_list(self, idNotification, fields=None):
        resp = requests.get(f"https://trello.com/1/notifications/{idNotification}/list", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_list_field(self, field, idNotification):
        resp = requests.get(f"https://trello.com/1/notifications/{idNotification}/list/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_member(self, idNotification, fields=None):
        resp = requests.get(f"https://trello.com/1/notifications/{idNotification}/member", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_member_field(self, field, idNotification):
        resp = requests.get(f"https://trello.com/1/notifications/{idNotification}/member/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_memberCreator(self, idNotification, fields=None):
        resp = requests.get(f"https://trello.com/1/notifications/{idNotification}/memberCreator", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_memberCreator_field(self, field, idNotification):
        resp = requests.get(f"https://trello.com/1/notifications/{idNotification}/memberCreator/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_organization(self, idNotification, fields=None):
        resp = requests.get(f"https://trello.com/1/notifications/{idNotification}/organization", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_organization_field(self, field, idNotification):
        resp = requests.get(f"https://trello.com/1/notifications/{idNotification}/organization/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def update(self, idNotification, unread=None):
        resp = requests.put(f"https://trello.com/1/notifications/{idNotification}", params={"key": self._apikey, "token": self._token}, data={"unread": unread})
        return self.raise_or_json(resp)

    def update_unread(self, idNotification, value):
        resp = requests.put(f"https://trello.com/1/notifications/{idNotification}/unread", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def new_all_read(self, ):
        resp = requests.post("https://trello.com/1/notifications/all/read", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)


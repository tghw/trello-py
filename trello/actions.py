from .base import ApiBase
import requests


class Actions(ApiBase):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idAction, display=None, entities=None, fields=None, member=None, member_fields=None, memberCreator=None, memberCreator_fields=None):
        resp = requests.get(f"https://trello.com/1/actions/{idAction}", params={"key": self._apikey, "token": self._token, "display": display, "entities": entities, "fields": fields, "member": member, "member_fields": member_fields, "memberCreator": memberCreator, "memberCreator_fields": memberCreator_fields}, data=None)
        return self.raise_or_json(resp)

    def get_field(self, field, idAction):
        resp = requests.get(f"https://trello.com/1/actions/{idAction}/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_board(self, idAction, fields=None):
        resp = requests.get(f"https://trello.com/1/actions/{idAction}/board", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_board_field(self, field, idAction):
        resp = requests.get(f"https://trello.com/1/actions/{idAction}/board/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_card(self, idAction, fields=None):
        resp = requests.get(f"https://trello.com/1/actions/{idAction}/card", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_card_field(self, field, idAction):
        resp = requests.get(f"https://trello.com/1/actions/{idAction}/card/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_display(self, idAction):
        resp = requests.get(f"https://trello.com/1/actions/{idAction}/display", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_entitie(self, idAction):
        resp = requests.get(f"https://trello.com/1/actions/{idAction}/entities", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_list(self, idAction, fields=None):
        resp = requests.get(f"https://trello.com/1/actions/{idAction}/list", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_list_field(self, field, idAction):
        resp = requests.get(f"https://trello.com/1/actions/{idAction}/list/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_member(self, idAction, fields=None):
        resp = requests.get(f"https://trello.com/1/actions/{idAction}/member", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_member_field(self, field, idAction):
        resp = requests.get(f"https://trello.com/1/actions/{idAction}/member/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_memberCreator(self, idAction, fields=None):
        resp = requests.get(f"https://trello.com/1/actions/{idAction}/memberCreator", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_memberCreator_field(self, field, idAction):
        resp = requests.get(f"https://trello.com/1/actions/{idAction}/memberCreator/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_organization(self, idAction, fields=None):
        resp = requests.get(f"https://trello.com/1/actions/{idAction}/organization", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_organization_field(self, field, idAction):
        resp = requests.get(f"https://trello.com/1/actions/{idAction}/organization/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def update(self, idAction, text=None):
        resp = requests.put(f"https://trello.com/1/actions/{idAction}", params={"key": self._apikey, "token": self._token}, data={"text": text})
        return self.raise_or_json(resp)

    def update_text(self, idAction, value):
        resp = requests.put(f"https://trello.com/1/actions/{idAction}/text", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def delete(self, idAction):
        resp = requests.delete(f"https://trello.com/1/actions/{idAction}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)


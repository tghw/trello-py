from .base import ApiBase
import requests

class Checklists(ApiBase):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idChecklist, cards=None, card_fields=None, checkItems=None, checkItem_fields=None, fields=None):
        resp = requests.get(f"https://trello.com/1/checklists/{idChecklist}", params={"key": self._apikey, "token": self._token, "cards": cards, "card_fields": card_fields, "checkItems": checkItems, "checkItem_fields": checkItem_fields, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_field(self, field, idChecklist):
        resp = requests.get(f"https://trello.com/1/checklists/{idChecklist}/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_board(self, idChecklist, fields=None):
        resp = requests.get(f"https://trello.com/1/checklists/{idChecklist}/board", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_board_field(self, field, idChecklist):
        resp = requests.get(f"https://trello.com/1/checklists/{idChecklist}/board/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_card(self, idChecklist, actions=None, attachments=None, attachment_fields=None, stickers=None, members=None, member_fields=None, checkItemStates=None, checklists=None, limit=None, since=None, before=None, filter=None, fields=None):
        resp = requests.get(f"https://trello.com/1/checklists/{idChecklist}/cards", params={"key": self._apikey, "token": self._token, "actions": actions, "attachments": attachments, "attachment_fields": attachment_fields, "stickers": stickers, "members": members, "member_fields": member_fields, "checkItemStates": checkItemStates, "checklists": checklists, "limit": limit, "since": since, "before": before, "filter": filter, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_card_filter(self, filter, idChecklist):
        resp = requests.get(f"https://trello.com/1/checklists/{idChecklist}/cards/{filter}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_checkItem(self, idChecklist, filter=None, fields=None):
        resp = requests.get(f"https://trello.com/1/checklists/{idChecklist}/checkItems", params={"key": self._apikey, "token": self._token, "filter": filter, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_checkItem_idCheckItem(self, idCheckItem, idChecklist, fields=None):
        resp = requests.get(f"https://trello.com/1/checklists/{idChecklist}/checkItems/{idCheckItem}", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def update(self, idChecklist, name=None, pos=None):
        resp = requests.put(f"https://trello.com/1/checklists/{idChecklist}", params={"key": self._apikey, "token": self._token}, data={"name": name, "pos": pos})
        return self.raise_or_json(resp)

    def update_name(self, idChecklist, value):
        resp = requests.put(f"https://trello.com/1/checklists/{idChecklist}/name", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_po(self, idChecklist, value):
        resp = requests.put(f"https://trello.com/1/checklists/{idChecklist}/pos", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def new(self, idCard, name=None, pos=None, idChecklistSource=None):
        resp = requests.post("https://trello.com/1/checklists", params={"key": self._apikey, "token": self._token}, data={"idCard": idCard, "name": name, "pos": pos, "idChecklistSource": idChecklistSource})
        return self.raise_or_json(resp)

    def new_checkItem(self, idChecklist, name, pos=None, checked=None, due=None):
        resp = requests.post(f"https://trello.com/1/checklists/{idChecklist}/checkItems", params={"key": self._apikey, "token": self._token}, data={"name": name, "pos": pos, "checked": checked, "due": due})
        return self.raise_or_json(resp)

    def delete(self, idChecklist):
        resp = requests.delete(f"https://trello.com/1/checklists/{idChecklist}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def delete_checkItem_idCheckItem(self, idCheckItem, idChecklist):
        resp = requests.delete(f"https://trello.com/1/checklists/{idChecklist}/checkItems/{idCheckItem}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)


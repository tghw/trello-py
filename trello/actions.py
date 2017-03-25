import json
import requests

class Actions(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idAction, display=None, entities=None, fields=None, member=None, member_fields=None, memberCreator=None, memberCreator_fields=None):
        resp = requests.get("https://trello.com/1/actions/{}".format(idAction), params={"key": self._apikey, "token": self._token, "display": display, "entities": entities, "fields": fields, "member": member, "member_fields": member_fields, "memberCreator": memberCreator, "memberCreator_fields": memberCreator_fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_field(self, field, idAction):
        resp = requests.get("https://trello.com/1/actions/{}/{}".format(idAction, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_board(self, idAction, fields=None):
        resp = requests.get("https://trello.com/1/actions/{}/board".format(idAction), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_board_field(self, field, idAction):
        resp = requests.get("https://trello.com/1/actions/{}/board/{}".format(idAction, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_card(self, idAction, fields=None):
        resp = requests.get("https://trello.com/1/actions/{}/card".format(idAction), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_card_field(self, field, idAction):
        resp = requests.get("https://trello.com/1/actions/{}/card/{}".format(idAction, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_display(self, idAction):
        resp = requests.get("https://trello.com/1/actions/{}/display".format(idAction), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_entitie(self, idAction):
        resp = requests.get("https://trello.com/1/actions/{}/entities".format(idAction), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_list(self, idAction, fields=None):
        resp = requests.get("https://trello.com/1/actions/{}/list".format(idAction), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_list_field(self, field, idAction):
        resp = requests.get("https://trello.com/1/actions/{}/list/{}".format(idAction, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_member(self, idAction, fields=None):
        resp = requests.get("https://trello.com/1/actions/{}/member".format(idAction), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_member_field(self, field, idAction):
        resp = requests.get("https://trello.com/1/actions/{}/member/{}".format(idAction, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_memberCreator(self, idAction, fields=None):
        resp = requests.get("https://trello.com/1/actions/{}/memberCreator".format(idAction), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_memberCreator_field(self, field, idAction):
        resp = requests.get("https://trello.com/1/actions/{}/memberCreator/{}".format(idAction, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_organization(self, idAction, fields=None):
        resp = requests.get("https://trello.com/1/actions/{}/organization".format(idAction), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_organization_field(self, field, idAction):
        resp = requests.get("https://trello.com/1/actions/{}/organization/{}".format(idAction, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def update(self, idAction, text=None):
        resp = requests.put("https://trello.com/1/actions/{}".format(idAction), params={"key": self._apikey, "token": self._token}, data={"text": text})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_text(self, idAction, value):
        resp = requests.put("https://trello.com/1/actions/{}/text".format(idAction), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def delete(self, idAction):
        resp = requests.delete("https://trello.com/1/actions/{}".format(idAction), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)


import json
import requests

class Boards(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, board_id, actions=None, action_fields=None, action_limit=None, cards=None, card_fields=None, lists=None, list_fields=None, members=None, member_fields=None, membersInvited=None, membersInvited_fields=None, checklists=None, checklist_fields=None, organization=None, organization_fields=None, myPrefs=None, fields=None):
        resp = requests.get("https://trello.com/1/boards/%s" % (board_id), params=dict(key=self._apikey, token=self._token, actions=actions, action_fields=action_fields, action_limit=action_limit, cards=cards, card_fields=card_fields, lists=lists, list_fields=list_fields, members=members, member_fields=member_fields, membersInvited=membersInvited, membersInvited_fields=membersInvited_fields, checklists=checklists, checklist_fields=checklist_fields, organization=organization, organization_fields=organization_fields, myPrefs=myPrefs, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_field(self, field, board_id):
        resp = requests.get("https://trello.com/1/boards/%s/%s" % (board_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_action(self, board_id, filter=None, fields=None, limit=None, page=None, idModels=None):
        resp = requests.get("https://trello.com/1/boards/%s/actions" % (board_id), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, limit=limit, page=page, idModels=idModels), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card(self, board_id, actions=None, attachments=None, members=None, checkItemStates=None, checklists=None, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/boards/%s/cards" % (board_id), params=dict(key=self._apikey, token=self._token, actions=actions, attachments=attachments, members=members, checkItemStates=checkItemStates, checklists=checklists, filter=filter, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card_filter(self, filter, board_id):
        resp = requests.get("https://trello.com/1/boards/%s/cards/%s" % (board_id, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card_idCard(self, idCard, board_id, actions=None, action_fields=None, action_limit=None, members=None, member_fields=None, checkItemStates=None, checkItemState_fields=None, labels=None, checklists=None, checklist_fields=None, fields=None):
        resp = requests.get("https://trello.com/1/boards/%s/cards/%s" % (board_id, idCard), params=dict(key=self._apikey, token=self._token, actions=actions, action_fields=action_fields, action_limit=action_limit, members=members, member_fields=member_fields, checkItemStates=checkItemStates, checkItemState_fields=checkItemState_fields, labels=labels, checklists=checklists, checklist_fields=checklist_fields, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_checklist(self, board_id, cards=None, card_fields=None, checkItems=None, checkItem_fields=None, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/boards/%s/checklists" % (board_id), params=dict(key=self._apikey, token=self._token, cards=cards, card_fields=card_fields, checkItems=checkItems, checkItem_fields=checkItem_fields, filter=filter, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_list(self, board_id, cards=None, card_fields=None, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/boards/%s/lists" % (board_id), params=dict(key=self._apikey, token=self._token, cards=cards, card_fields=card_fields, filter=filter, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_list_filter(self, filter, board_id):
        resp = requests.get("https://trello.com/1/boards/%s/lists/%s" % (board_id, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member(self, board_id, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/boards/%s/members" % (board_id), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member_filter(self, filter, board_id):
        resp = requests.get("https://trello.com/1/boards/%s/members/%s" % (board_id, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_membersInvited(self, board_id, fields=None):
        resp = requests.get("https://trello.com/1/boards/%s/membersInvited" % (board_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_membersInvited_field(self, field, board_id):
        resp = requests.get("https://trello.com/1/boards/%s/membersInvited/%s" % (board_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_myPref(self, board_id):
        resp = requests.get("https://trello.com/1/boards/%s/myPrefs" % (board_id), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_organization(self, board_id, fields=None):
        resp = requests.get("https://trello.com/1/boards/%s/organization" % (board_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_organization_field(self, field, board_id):
        resp = requests.get("https://trello.com/1/boards/%s/organization/%s" % (board_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def update(self, board_id, name=None, desc=None, closed=None):
        resp = requests.put("https://trello.com/1/boards/%s" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(name=name, desc=desc, closed=closed))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_closed(self, board_id, value):
        resp = requests.put("https://trello.com/1/boards/%s/closed" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_desc(self, board_id, value):
        resp = requests.put("https://trello.com/1/boards/%s/desc" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_name(self, board_id, value):
        resp = requests.put("https://trello.com/1/boards/%s/name" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new(self, name, desc=None, idOrganization=None):
        resp = requests.post("https://trello.com/1/boards" % (), params=dict(key=self._apikey, token=self._token), data=dict(name=name, desc=desc, idOrganization=idOrganization))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_checklist(self, board_id, name):
        resp = requests.post("https://trello.com/1/boards/%s/checklists" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(name=name))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_list(self, board_id, name):
        resp = requests.post("https://trello.com/1/boards/%s/lists" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(name=name))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_myPref(self, board_id, name, value):
        resp = requests.post("https://trello.com/1/boards/%s/myPrefs" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(name=name, value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    

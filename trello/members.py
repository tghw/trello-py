import json
import requests

class Members(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, member_id_or_username, actions=None, action_fields=None, action_limit=None, cards=None, card_fields=None, boards=None, board_fields=None, boardsInvited=None, boardsInvited_fields=None, organizations=None, organization_fields=None, organizationsInvited=None, organizationsInvited_fields=None, notifications=None, notification_fields=None, notification_limit=None, fields=None):
        resp = requests.get("https://trello.com/1/members/%s" % (member_id_or_username), params=dict(key=self._apikey, token=self._token, actions=actions, action_fields=action_fields, action_limit=action_limit, cards=cards, card_fields=card_fields, boards=boards, board_fields=board_fields, boardsInvited=boardsInvited, boardsInvited_fields=boardsInvited_fields, organizations=organizations, organization_fields=organization_fields, organizationsInvited=organizationsInvited, organizationsInvited_fields=organizationsInvited_fields, notifications=notifications, notification_fields=notification_fields, notification_limit=notification_limit, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_field(self, field, member_id_or_username):
        resp = requests.get("https://trello.com/1/members/%s/%s" % (member_id_or_username, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_action(self, member_id_or_username, filter=None, fields=None, limit=None, page=None, idModels=None):
        resp = requests.get("https://trello.com/1/members/%s/actions" % (member_id_or_username), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, limit=limit, page=page, idModels=idModels), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board(self, member_id_or_username, filter=None, fields=None, actions=None, action_fields=None, action_limit=None):
        resp = requests.get("https://trello.com/1/members/%s/boards" % (member_id_or_username), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, actions=actions, action_fields=action_fields, action_limit=action_limit), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board_filter(self, filter, member_id_or_username):
        resp = requests.get("https://trello.com/1/members/%s/boards/%s" % (member_id_or_username, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_boardsInvited(self, member_id_or_username, fields=None):
        resp = requests.get("https://trello.com/1/members/%s/boardsInvited" % (member_id_or_username), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_boardsInvited_field(self, field, member_id_or_username):
        resp = requests.get("https://trello.com/1/members/%s/boardsInvited/%s" % (member_id_or_username, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card(self, member_id_or_username, actions=None, attachments=None, members=None, checkItemStates=None, checklists=None, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/members/%s/cards" % (member_id_or_username), params=dict(key=self._apikey, token=self._token, actions=actions, attachments=attachments, members=members, checkItemStates=checkItemStates, checklists=checklists, filter=filter, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card_filter(self, filter, member_id_or_username):
        resp = requests.get("https://trello.com/1/members/%s/cards/%s" % (member_id_or_username, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_notification(self, member_id_or_username, filter=None, read_filter=None, fields=None, limit=None, page=None):
        resp = requests.get("https://trello.com/1/members/%s/notifications" % (member_id_or_username), params=dict(key=self._apikey, token=self._token, filter=filter, read_filter=read_filter, fields=fields, limit=limit, page=page), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_notification_filter(self, filter, member_id_or_username):
        resp = requests.get("https://trello.com/1/members/%s/notifications/%s" % (member_id_or_username, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_organization(self, member_id_or_username, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/members/%s/organizations" % (member_id_or_username), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_organization_filter(self, filter, member_id_or_username):
        resp = requests.get("https://trello.com/1/members/%s/organizations/%s" % (member_id_or_username, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_organizationsInvited(self, member_id_or_username, fields=None):
        resp = requests.get("https://trello.com/1/members/%s/organizationsInvited" % (member_id_or_username), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_organizationsInvited_field(self, field, member_id_or_username):
        resp = requests.get("https://trello.com/1/members/%s/organizationsInvited/%s" % (member_id_or_username, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def update(self, member_id_or_username, fullName=None, initials=None, bio=None):
        resp = requests.put("https://trello.com/1/members/%s" % (member_id_or_username), params=dict(key=self._apikey, token=self._token), data=dict(fullName=fullName, initials=initials, bio=bio))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_bio(self, member_id_or_username, value):
        resp = requests.put("https://trello.com/1/members/%s/bio" % (member_id_or_username), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_fullName(self, member_id_or_username, value):
        resp = requests.put("https://trello.com/1/members/%s/fullName" % (member_id_or_username), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_initial(self, member_id_or_username, value):
        resp = requests.put("https://trello.com/1/members/%s/initials" % (member_id_or_username), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    

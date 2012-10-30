import json
import requests

class Members(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idMember_or_username, actions=None, actions_entities=None, actions_limit=None, action_fields=None, cards=None, card_fields=None, card_members=None, card_member_fields=None, card_attachments=None, card_attachment_fields=None, boards=None, board_fields=None, board_actions=None, board_actions_entities=None, board_actions_format=None, board_actions_since=None, board_actions_limit=None, board_action_fields=None, board_lists=None, board_organization=None, board_organization_fields=None, boardsInvited=None, boardsInvited_fields=None, organizations=None, organization_fields=None, organization_paid_account=None, organizationsInvited=None, organizationsInvited_fields=None, notifications=None, notifications_entities=None, notifications_limit=None, notification_fields=None, tokens=None, fields=None):
        resp = requests.get("https://trello.com/1/members/%s" % (idMember_or_username), params=dict(key=self._apikey, token=self._token, actions=actions, actions_entities=actions_entities, actions_limit=actions_limit, action_fields=action_fields, cards=cards, card_fields=card_fields, card_members=card_members, card_member_fields=card_member_fields, card_attachments=card_attachments, card_attachment_fields=card_attachment_fields, boards=boards, board_fields=board_fields, board_actions=board_actions, board_actions_entities=board_actions_entities, board_actions_format=board_actions_format, board_actions_since=board_actions_since, board_actions_limit=board_actions_limit, board_action_fields=board_action_fields, board_lists=board_lists, board_organization=board_organization, board_organization_fields=board_organization_fields, boardsInvited=boardsInvited, boardsInvited_fields=boardsInvited_fields, organizations=organizations, organization_fields=organization_fields, organization_paid_account=organization_paid_account, organizationsInvited=organizationsInvited, organizationsInvited_fields=organizationsInvited_fields, notifications=notifications, notifications_entities=notifications_entities, notifications_limit=notifications_limit, notification_fields=notification_fields, tokens=tokens, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_field(self, field, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/%s/%s" % (idMember_or_username, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_action(self, idMember_or_username, entities=None, filter=None, fields=None, limit=None, format=None, since=None, page=None, idModels=None):
        resp = requests.get("https://trello.com/1/members/%s/actions" % (idMember_or_username), params=dict(key=self._apikey, token=self._token, entities=entities, filter=filter, fields=fields, limit=limit, format=format, since=since, page=page, idModels=idModels), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board(self, idMember_or_username, filter=None, fields=None, actions=None, actions_entities=None, actions_limit=None, actions_format=None, actions_since=None, action_fields=None, organization=None, organization_fields=None, lists=None):
        resp = requests.get("https://trello.com/1/members/%s/boards" % (idMember_or_username), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, actions=actions, actions_entities=actions_entities, actions_limit=actions_limit, actions_format=actions_format, actions_since=actions_since, action_fields=action_fields, organization=organization, organization_fields=organization_fields, lists=lists), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board_filter(self, filter, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/%s/boards/%s" % (idMember_or_username, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_boardsInvited(self, idMember_or_username, fields=None):
        resp = requests.get("https://trello.com/1/members/%s/boardsInvited" % (idMember_or_username), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_boardsInvited_field(self, field, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/%s/boardsInvited/%s" % (idMember_or_username, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card(self, idMember_or_username, actions=None, attachments=None, attachment_fields=None, members=None, member_fields=None, checkItemStates=None, checklists=None, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/members/%s/cards" % (idMember_or_username), params=dict(key=self._apikey, token=self._token, actions=actions, attachments=attachments, attachment_fields=attachment_fields, members=members, member_fields=member_fields, checkItemStates=checkItemStates, checklists=checklists, filter=filter, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card_filter(self, filter, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/%s/cards/%s" % (idMember_or_username, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_notification(self, idMember_or_username, entities=None, filter=None, read_filter=None, fields=None, limit=None, page=None, before=None, since=None):
        resp = requests.get("https://trello.com/1/members/%s/notifications" % (idMember_or_username), params=dict(key=self._apikey, token=self._token, entities=entities, filter=filter, read_filter=read_filter, fields=fields, limit=limit, page=page, before=before, since=since), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_notification_filter(self, filter, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/%s/notifications/%s" % (idMember_or_username, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_organization(self, idMember_or_username, filter=None, fields=None, paid_account=None):
        resp = requests.get("https://trello.com/1/members/%s/organizations" % (idMember_or_username), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, paid_account=paid_account), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_organization_filter(self, filter, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/%s/organizations/%s" % (idMember_or_username, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_organizationsInvited(self, idMember_or_username, fields=None):
        resp = requests.get("https://trello.com/1/members/%s/organizationsInvited" % (idMember_or_username), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_organizationsInvited_field(self, field, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/%s/organizationsInvited/%s" % (idMember_or_username, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_token(self, idMember_or_username, filter=None):
        resp = requests.get("https://trello.com/1/members/%s/tokens" % (idMember_or_username), params=dict(key=self._apikey, token=self._token, filter=filter), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def update(self, idMember_or_username, fullName=None, initials=None, bio=None):
        resp = requests.put("https://trello.com/1/members/%s" % (idMember_or_username), params=dict(key=self._apikey, token=self._token), data=dict(fullName=fullName, initials=initials, bio=bio))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_bio(self, idMember_or_username, value):
        resp = requests.put("https://trello.com/1/members/%s/bio" % (idMember_or_username), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_fullName(self, idMember_or_username, value):
        resp = requests.put("https://trello.com/1/members/%s/fullName" % (idMember_or_username), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_initial(self, idMember_or_username, value):
        resp = requests.put("https://trello.com/1/members/%s/initials" % (idMember_or_username), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)


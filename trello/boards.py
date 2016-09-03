import json
import requests

class Boards(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, board_id, actions=None, actions_entities=None, actions_format=None, actions_since=None, actions_limit=None, action_fields=None, cards=None, card_fields=None, card_attachments=None, card_attachment_fields=None, lists=None, list_fields=None, members=None, member_fields=None, membersInvited=None, membersInvited_fields=None, checklists=None, checklist_fields=None, organization=None, organization_fields=None, myPrefs=None, fields=None):
        resp = requests.get("https://trello.com/1/boards/%s" % (board_id), params=dict(key=self._apikey, token=self._token, actions=actions, actions_entities=actions_entities, actions_format=actions_format, actions_since=actions_since, actions_limit=actions_limit, action_fields=action_fields, cards=cards, card_fields=card_fields, card_attachments=card_attachments, card_attachment_fields=card_attachment_fields, lists=lists, list_fields=list_fields, members=members, member_fields=member_fields, membersInvited=membersInvited, membersInvited_fields=membersInvited_fields, checklists=checklists, checklist_fields=checklist_fields, organization=organization, organization_fields=organization_fields, myPrefs=myPrefs, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_field(self, field, board_id):
        resp = requests.get("https://trello.com/1/boards/%s/%s" % (board_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_action(self, board_id, entities=None, filter=None, fields=None, limit=None, format=None, since=None, page=None, idModels=None):
        resp = requests.get("https://trello.com/1/boards/%s/actions" % (board_id), params=dict(key=self._apikey, token=self._token, entities=entities, filter=filter, fields=fields, limit=limit, format=format, since=since, page=page, idModels=idModels), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card(self, board_id, actions=None, attachments=None, attachment_fields=None, members=None, member_fields=None, checkItemStates=None, checklists=None, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/boards/%s/cards" % (board_id), params=dict(key=self._apikey, token=self._token, actions=actions, attachments=attachments, attachment_fields=attachment_fields, members=members, member_fields=member_fields, checkItemStates=checkItemStates, checklists=checklists, filter=filter, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card_filter(self, filter, board_id):
        resp = requests.get("https://trello.com/1/boards/%s/cards/%s" % (board_id, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_card_idCard(self, idCard, board_id, attachments=None, attachment_fields=None, actions=None, actions_entities=None, actions_limit=None, action_fields=None, members=None, member_fields=None, checkItemStates=None, checkItemState_fields=None, labels=None, checklists=None, checklist_fields=None, fields=None):
        resp = requests.get("https://trello.com/1/boards/%s/cards/%s" % (board_id, idCard), params=dict(key=self._apikey, token=self._token, attachments=attachments, attachment_fields=attachment_fields, actions=actions, actions_entities=actions_entities, actions_limit=actions_limit, action_fields=action_fields, members=members, member_fields=member_fields, checkItemStates=checkItemStates, checkItemState_fields=checkItemState_fields, labels=labels, checklists=checklists, checklist_fields=checklist_fields, fields=fields), data=None)
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

    def get_member(self, board_id, filter=None, fields=None, activity=None):
        resp = requests.get("https://trello.com/1/boards/%s/members" % (board_id), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, activity=activity), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member_filter(self, filter, board_id):
        resp = requests.get("https://trello.com/1/boards/%s/members/%s" % (board_id, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member_card_idMember(self, idMember, board_id, actions=None, attachments=None, attachment_fields=None, members=None, member_fields=None, checkItemStates=None, checklists=None, board=None, board_fields=None, list=None, list_fields=None, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/boards/%s/members/%s/cards" % (board_id, idMember), params=dict(key=self._apikey, token=self._token, actions=actions, attachments=attachments, attachment_fields=attachment_fields, members=members, member_fields=member_fields, checkItemStates=checkItemStates, checklists=checklists, board=board, board_fields=board_fields, list=list, list_fields=list_fields, filter=filter, fields=fields), data=None)
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

    def update(self, board_id, name=None, desc=None, closed=None, subscribed=None, idOrganization=None, permissionLevel=None, selfJoin=None, cardCovers=None, invitations=None, voting=None, comments=None):
        resp = requests.put("https://trello.com/1/boards/%s" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(name=name, desc=desc, closed=closed, subscribed=subscribed, idOrganization=idOrganization, permissionLevel=permissionLevel, selfJoin=selfJoin, cardCovers=cardCovers, invitations=invitations, voting=voting, comments=comments))
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

    def update_idOrganization(self, board_id, value):
        resp = requests.put("https://trello.com/1/boards/%s/idOrganization" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_member_idMember(self, idMember, board_id, type):
        resp = requests.put("https://trello.com/1/boards/%s/members/%s" % (board_id, idMember), params=dict(key=self._apikey, token=self._token), data=dict(type=type))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_name(self, board_id, value):
        resp = requests.put("https://trello.com/1/boards/%s/name" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_pref_cardCover(self, board_id, value):
        resp = requests.put("https://trello.com/1/boards/%s/prefs/cardCovers" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_pref_comment(self, board_id, value):
        resp = requests.put("https://trello.com/1/boards/%s/prefs/comments" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_pref_invitation(self, board_id, value):
        resp = requests.put("https://trello.com/1/boards/%s/prefs/invitations" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_pref_permissionLevel(self, board_id, value):
        resp = requests.put("https://trello.com/1/boards/%s/prefs/permissionLevel" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_pref_selfJoin(self, board_id, value):
        resp = requests.put("https://trello.com/1/boards/%s/prefs/selfJoin" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_pref_voting(self, board_id, value):
        resp = requests.put("https://trello.com/1/boards/%s/prefs/voting" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_subscribed(self, board_id, value):
        resp = requests.put("https://trello.com/1/boards/%s/subscribed" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new(self, name, desc=None, idOrganization=None, idBoardSource=None, keepFromSource=None, prefs_permissionLevel=None, prefs_voting=None, prefs_comments=None, prefs_invitations=None, prefs_selfJoin=None, prefs_cardCovers=None):
        resp = requests.post("https://trello.com/1/boards" % (), params=dict(key=self._apikey, token=self._token), data=dict(name=name, desc=desc, idOrganization=idOrganization, idBoardSource=idBoardSource, keepFromSource=keepFromSource, prefs_permissionLevel=prefs_permissionLevel, prefs_voting=prefs_voting, prefs_comments=prefs_comments, prefs_invitations=prefs_invitations, prefs_selfJoin=prefs_selfJoin, prefs_cardCovers=prefs_cardCovers))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_checklist(self, board_id, name):
        resp = requests.post("https://trello.com/1/boards/%s/checklists" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(name=name))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_invitation(self, board_id, idMember=None, email=None, type=None):
        resp = requests.post("https://trello.com/1/boards/%s/invitations" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(idMember=idMember, email=email, type=type))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_invitation_response(self, response, board_id, invitationTokens=None):
        resp = requests.post("https://trello.com/1/boards/%s/invitations/%s" % (board_id, response), params=dict(key=self._apikey, token=self._token), data=dict(invitationTokens=invitationTokens))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_list(self, board_id, name, pos=None):
        resp = requests.post("https://trello.com/1/boards/%s/lists" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(name=name, pos=pos))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_markAsViewed(self, board_id):
        resp = requests.post("https://trello.com/1/boards/%s/markAsViewed" % (board_id), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_myPref(self, board_id, name, value):
        resp = requests.post("https://trello.com/1/boards/%s/myPrefs" % (board_id), params=dict(key=self._apikey, token=self._token), data=dict(name=name, value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete_invitation_idInvitation(self, idInvitation, board_id):
        resp = requests.delete("https://trello.com/1/boards/%s/invitations/%s" % (board_id, idInvitation), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete_member_idMember(self, idMember, board_id):
        resp = requests.delete("https://trello.com/1/boards/%s/members/%s" % (board_id, idMember), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

import json
import requests

class Organizations(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idOrg_or_name, actions=None, actions_entities=None, actions_display=None, actions_limit=None, action_fields=None, memberships=None, memberships_member=None, memberships_member_fields=None, members=None, member_fields=None, member_activity=None, membersInvited=None, membersInvited_fields=None, pluginData=None, boards=None, board_fields=None, board_actions=None, board_actions_entities=None, board_actions_display=None, board_actions_format=None, board_actions_since=None, board_actions_limit=None, board_action_fields=None, board_lists=None, board_pluginData=None, paid_account=None, fields=None):
        resp = requests.get("https://trello.com/1/organizations/%s" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token, actions=actions, actions_entities=actions_entities, actions_display=actions_display, actions_limit=actions_limit, action_fields=action_fields, memberships=memberships, memberships_member=memberships_member, memberships_member_fields=memberships_member_fields, members=members, member_fields=member_fields, member_activity=member_activity, membersInvited=membersInvited, membersInvited_fields=membersInvited_fields, pluginData=pluginData, boards=boards, board_fields=board_fields, board_actions=board_actions, board_actions_entities=board_actions_entities, board_actions_display=board_actions_display, board_actions_format=board_actions_format, board_actions_since=board_actions_since, board_actions_limit=board_actions_limit, board_action_fields=board_action_fields, board_lists=board_lists, board_pluginData=board_pluginData, paid_account=paid_account, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_field(self, field, idOrg_or_name):
        resp = requests.get("https://trello.com/1/organizations/%s/%s" % (idOrg_or_name, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_action(self, idOrg_or_name, entities=None, display=None, filter=None, fields=None, limit=None, format=None, since=None, before=None, page=None, idModels=None, member=None, member_fields=None, memberCreator=None, memberCreator_fields=None):
        resp = requests.get("https://trello.com/1/organizations/%s/actions" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token, entities=entities, display=display, filter=filter, fields=fields, limit=limit, format=format, since=since, before=before, page=page, idModels=idModels, member=member, member_fields=member_fields, memberCreator=memberCreator, memberCreator_fields=memberCreator_fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board(self, idOrg_or_name, filter=None, fields=None, actions=None, actions_entities=None, actions_limit=None, actions_format=None, actions_since=None, action_fields=None, memberships=None, organization=None, organization_fields=None, lists=None):
        resp = requests.get("https://trello.com/1/organizations/%s/boards" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, actions=actions, actions_entities=actions_entities, actions_limit=actions_limit, actions_format=actions_format, actions_since=actions_since, action_fields=action_fields, memberships=memberships, organization=organization, organization_fields=organization_fields, lists=lists), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board_filter(self, filter, idOrg_or_name):
        resp = requests.get("https://trello.com/1/organizations/%s/boards/%s" % (idOrg_or_name, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_delta(self, idOrg_or_name, tags, ixLastUpdate):
        resp = requests.get("https://trello.com/1/organizations/%s/deltas" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token, tags=tags, ixLastUpdate=ixLastUpdate), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member(self, idOrg_or_name, filter=None, fields=None, activity=None):
        resp = requests.get("https://trello.com/1/organizations/%s/members" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, activity=activity), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member_filter(self, filter, idOrg_or_name):
        resp = requests.get("https://trello.com/1/organizations/%s/members/%s" % (idOrg_or_name, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member_card_idMember(self, idMember, idOrg_or_name, actions=None, attachments=None, attachment_fields=None, members=None, member_fields=None, checkItemStates=None, checklists=None, board=None, board_fields=None, list=None, list_fields=None, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/organizations/%s/members/%s/cards" % (idOrg_or_name, idMember), params=dict(key=self._apikey, token=self._token, actions=actions, attachments=attachments, attachment_fields=attachment_fields, members=members, member_fields=member_fields, checkItemStates=checkItemStates, checklists=checklists, board=board, board_fields=board_fields, list=list, list_fields=list_fields, filter=filter, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_membersInvited(self, idOrg_or_name, fields=None):
        resp = requests.get("https://trello.com/1/organizations/%s/membersInvited" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_membersInvited_field(self, field, idOrg_or_name):
        resp = requests.get("https://trello.com/1/organizations/%s/membersInvited/%s" % (idOrg_or_name, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_membership(self, idOrg_or_name, filter=None, member=None):
        resp = requests.get("https://trello.com/1/organizations/%s/memberships" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token, filter=filter, member=member), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_membership_idMembership(self, idMembership, idOrg_or_name, member=None):
        resp = requests.get("https://trello.com/1/organizations/%s/memberships/%s" % (idOrg_or_name, idMembership), params=dict(key=self._apikey, token=self._token, member=member), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_pluginData(self, idOrg_or_name):
        resp = requests.get("https://trello.com/1/organizations/%s/pluginData" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def update(self, idOrg_or_name, prefs/orgInviteRestrict=None, prefs/externalMembersDisabled=None, prefs/associatedDomain=None, prefs/googleAppsVersion=None, prefs/boardVisibilityRestrict/private=None, prefs/boardVisibilityRestrict/org=None, prefs/boardVisibilityRestrict/public=None, name=None, displayName=None, desc=None, website=None, prefs/permissionLevel=None):
        resp = requests.put("https://trello.com/1/organizations/%s" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(prefs/orgInviteRestrict=prefs/orgInviteRestrict, prefs/externalMembersDisabled=prefs/externalMembersDisabled, prefs/associatedDomain=prefs/associatedDomain, prefs/googleAppsVersion=prefs/googleAppsVersion, prefs/boardVisibilityRestrict/private=prefs/boardVisibilityRestrict/private, prefs/boardVisibilityRestrict/org=prefs/boardVisibilityRestrict/org, prefs/boardVisibilityRestrict/public=prefs/boardVisibilityRestrict/public, name=name, displayName=displayName, desc=desc, website=website, prefs/permissionLevel=prefs/permissionLevel))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_desc(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/desc" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_displayName(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/displayName" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_member(self, idOrg_or_name, email, fullName, type=None):
        resp = requests.put("https://trello.com/1/organizations/%s/members" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(email=email, fullName=fullName, type=type))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_member_idMember(self, idMember, idOrg_or_name, type):
        resp = requests.put("https://trello.com/1/organizations/%s/members/%s" % (idOrg_or_name, idMember), params=dict(key=self._apikey, token=self._token), data=dict(type=type))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_member_deactivated_idMember(self, idMember, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/members/%s/deactivated" % (idOrg_or_name, idMember), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_membership_idMembership(self, idMembership, idOrg_or_name, type, member_fields=None):
        resp = requests.put("https://trello.com/1/organizations/%s/memberships/%s" % (idOrg_or_name, idMembership), params=dict(key=self._apikey, token=self._token), data=dict(type=type, member_fields=member_fields))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_name(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/name" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_pref_associatedDomain(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/prefs/associatedDomain" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_pref_boardVisibilityRestrict_org(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/prefs/boardVisibilityRestrict/org" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_pref_boardVisibilityRestrict_private(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/prefs/boardVisibilityRestrict/private" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_pref_boardVisibilityRestrict_public(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/prefs/boardVisibilityRestrict/public" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_pref_externalMembersDisabled(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/prefs/externalMembersDisabled" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_pref_googleAppsVersion(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/prefs/googleAppsVersion" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_pref_orgInviteRestrict(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/prefs/orgInviteRestrict" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_pref_permissionLevel(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/prefs/permissionLevel" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_website(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/website" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new(self, name=None, displayName=None, desc=None, website=None):
        resp = requests.post("https://trello.com/1/organizations" % (), params=dict(key=self._apikey, token=self._token), data=dict(name=name, displayName=displayName, desc=desc, website=website))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_logo(self, idOrg_or_name, file):
        resp = requests.post("https://trello.com/1/organizations/%s/logo" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=dict(file=file))
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete(self, idOrg_or_name):
        resp = requests.delete("https://trello.com/1/organizations/%s" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete_logo(self, idOrg_or_name):
        resp = requests.delete("https://trello.com/1/organizations/%s/logo" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete_member_idMember(self, idMember, idOrg_or_name):
        resp = requests.delete("https://trello.com/1/organizations/%s/members/%s" % (idOrg_or_name, idMember), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete_member_all_idMember(self, idMember, idOrg_or_name):
        resp = requests.delete("https://trello.com/1/organizations/%s/members/%s/all" % (idOrg_or_name, idMember), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete_pref_associatedDomain(self, idOrg_or_name):
        resp = requests.delete("https://trello.com/1/organizations/%s/prefs/associatedDomain" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete_pref_orgInviteRestrict(self, idOrg_or_name, value):
        resp = requests.delete("https://trello.com/1/organizations/%s/prefs/orgInviteRestrict" % (idOrg_or_name), params=dict(key=self._apikey, token=self._token, value=value), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)


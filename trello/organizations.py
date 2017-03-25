import json
import requests

class Organizations(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idOrg_or_name, actions=None, actions_entities=None, actions_display=None, actions_limit=None, action_fields=None, memberships=None, memberships_member=None, memberships_member_fields=None, members=None, member_fields=None, member_activity=None, membersInvited=None, membersInvited_fields=None, pluginData=None, boards=None, board_fields=None, board_actions=None, board_actions_entities=None, board_actions_display=None, board_actions_format=None, board_actions_since=None, board_actions_limit=None, board_action_fields=None, board_lists=None, board_pluginData=None, paid_account=None, fields=None):
        resp = requests.get("https://trello.com/1/organizations/{}".format(idOrg_or_name), params={"key": self._apikey, "token": self._token, "actions": actions, "actions_entities": actions_entities, "actions_display": actions_display, "actions_limit": actions_limit, "action_fields": action_fields, "memberships": memberships, "memberships_member": memberships_member, "memberships_member_fields": memberships_member_fields, "members": members, "member_fields": member_fields, "member_activity": member_activity, "membersInvited": membersInvited, "membersInvited_fields": membersInvited_fields, "pluginData": pluginData, "boards": boards, "board_fields": board_fields, "board_actions": board_actions, "board_actions_entities": board_actions_entities, "board_actions_display": board_actions_display, "board_actions_format": board_actions_format, "board_actions_since": board_actions_since, "board_actions_limit": board_actions_limit, "board_action_fields": board_action_fields, "board_lists": board_lists, "board_pluginData": board_pluginData, "paid_account": paid_account, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_field(self, field, idOrg_or_name):
        resp = requests.get("https://trello.com/1/organizations/{}/{}".format(idOrg_or_name, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_action(self, idOrg_or_name, entities=None, display=None, filter=None, fields=None, limit=None, format=None, since=None, before=None, page=None, idModels=None, member=None, member_fields=None, memberCreator=None, memberCreator_fields=None):
        resp = requests.get("https://trello.com/1/organizations/{}/actions".format(idOrg_or_name), params={"key": self._apikey, "token": self._token, "entities": entities, "display": display, "filter": filter, "fields": fields, "limit": limit, "format": format, "since": since, "before": before, "page": page, "idModels": idModels, "member": member, "member_fields": member_fields, "memberCreator": memberCreator, "memberCreator_fields": memberCreator_fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_board(self, idOrg_or_name, filter=None, fields=None, actions=None, actions_entities=None, actions_limit=None, actions_format=None, actions_since=None, action_fields=None, memberships=None, organization=None, organization_fields=None, lists=None):
        resp = requests.get("https://trello.com/1/organizations/{}/boards".format(idOrg_or_name), params={"key": self._apikey, "token": self._token, "filter": filter, "fields": fields, "actions": actions, "actions_entities": actions_entities, "actions_limit": actions_limit, "actions_format": actions_format, "actions_since": actions_since, "action_fields": action_fields, "memberships": memberships, "organization": organization, "organization_fields": organization_fields, "lists": lists}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_board_filter(self, filter, idOrg_or_name):
        resp = requests.get("https://trello.com/1/organizations/{}/boards/{}".format(idOrg_or_name, filter), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_delta(self, idOrg_or_name, tags, ixLastUpdate):
        resp = requests.get("https://trello.com/1/organizations/{}/deltas".format(idOrg_or_name), params={"key": self._apikey, "token": self._token, "tags": tags, "ixLastUpdate": ixLastUpdate}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_member(self, idOrg_or_name, filter=None, fields=None, activity=None):
        resp = requests.get("https://trello.com/1/organizations/{}/members".format(idOrg_or_name), params={"key": self._apikey, "token": self._token, "filter": filter, "fields": fields, "activity": activity}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_member_filter(self, filter, idOrg_or_name):
        resp = requests.get("https://trello.com/1/organizations/{}/members/{}".format(idOrg_or_name, filter), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_member_card_idMember(self, idMember, idOrg_or_name, actions=None, attachments=None, attachment_fields=None, members=None, member_fields=None, checkItemStates=None, checklists=None, board=None, board_fields=None, list=None, list_fields=None, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/organizations/{}/members/{}/cards".format(idOrg_or_name, idMember), params={"key": self._apikey, "token": self._token, "actions": actions, "attachments": attachments, "attachment_fields": attachment_fields, "members": members, "member_fields": member_fields, "checkItemStates": checkItemStates, "checklists": checklists, "board": board, "board_fields": board_fields, "list": list, "list_fields": list_fields, "filter": filter, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_membersInvited(self, idOrg_or_name, fields=None):
        resp = requests.get("https://trello.com/1/organizations/{}/membersInvited".format(idOrg_or_name), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_membersInvited_field(self, field, idOrg_or_name):
        resp = requests.get("https://trello.com/1/organizations/{}/membersInvited/{}".format(idOrg_or_name, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_membership(self, idOrg_or_name, filter=None, member=None):
        resp = requests.get("https://trello.com/1/organizations/{}/memberships".format(idOrg_or_name), params={"key": self._apikey, "token": self._token, "filter": filter, "member": member}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_membership_idMembership(self, idMembership, idOrg_or_name, member=None):
        resp = requests.get("https://trello.com/1/organizations/{}/memberships/{}".format(idOrg_or_name, idMembership), params={"key": self._apikey, "token": self._token, "member": member}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_pluginData(self, idOrg_or_name):
        resp = requests.get("https://trello.com/1/organizations/{}/pluginData".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def update(self, idOrg_or_name, prefs_orgInviteRestrict=None, prefs_externalMembersDisabled=None, prefs_associatedDomain=None, prefs_googleAppsVersion=None, prefs_boardVisibilityRestrict_private=None, prefs_boardVisibilityRestrict_org=None, prefs_boardVisibilityRestrict_public=None, name=None, displayName=None, desc=None, website=None, prefs_permissionLevel=None):
        resp = requests.put("https://trello.com/1/organizations/{}".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data={"prefs/orgInviteRestrict": prefs_orgInviteRestrict, "prefs/externalMembersDisabled": prefs_externalMembersDisabled, "prefs/associatedDomain": prefs_associatedDomain, "prefs/googleAppsVersion": prefs_googleAppsVersion, "prefs/boardVisibilityRestrict/private": prefs_boardVisibilityRestrict_private, "prefs/boardVisibilityRestrict/org": prefs_boardVisibilityRestrict_org, "prefs/boardVisibilityRestrict/public": prefs_boardVisibilityRestrict_public, "name": name, "displayName": displayName, "desc": desc, "website": website, "prefs/permissionLevel": prefs_permissionLevel})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_desc(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/{}/desc".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_displayName(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/{}/displayName".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_member(self, idOrg_or_name, email, fullName, type=None):
        resp = requests.put("https://trello.com/1/organizations/{}/members".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data={"email": email, "fullName": fullName, "type": type})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_member_idMember(self, idMember, idOrg_or_name, type):
        resp = requests.put("https://trello.com/1/organizations/{}/members/{}".format(idOrg_or_name, idMember), params={"key": self._apikey, "token": self._token}, data={"type": type})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_member_deactivated_idMember(self, idMember, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/{}/members/{}/deactivated".format(idOrg_or_name, idMember), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_membership_idMembership(self, idMembership, idOrg_or_name, type, member_fields=None):
        resp = requests.put("https://trello.com/1/organizations/{}/memberships/{}".format(idOrg_or_name, idMembership), params={"key": self._apikey, "token": self._token}, data={"type": type, "member_fields": member_fields})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_name(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/{}/name".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_pref_associatedDomain(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/{}/prefs/associatedDomain".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_pref_boardVisibilityRestrict_org(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/{}/prefs/boardVisibilityRestrict/org".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_pref_boardVisibilityRestrict_private(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/{}/prefs/boardVisibilityRestrict/private".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_pref_boardVisibilityRestrict_public(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/{}/prefs/boardVisibilityRestrict/public".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_pref_externalMembersDisabled(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/{}/prefs/externalMembersDisabled".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_pref_googleAppsVersion(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/{}/prefs/googleAppsVersion".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_pref_orgInviteRestrict(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/{}/prefs/orgInviteRestrict".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_pref_permissionLevel(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/{}/prefs/permissionLevel".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_website(self, idOrg_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/{}/website".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def new(self, name=None, displayName=None, desc=None, website=None):
        resp = requests.post("https://trello.com/1/organizations".format(), params={"key": self._apikey, "token": self._token}, data={"name": name, "displayName": displayName, "desc": desc, "website": website})
        resp.raise_for_status()
        return json.loads(resp.text)

    def new_logo(self, idOrg_or_name, file):
        resp = requests.post("https://trello.com/1/organizations/{}/logo".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data={"file": file})
        resp.raise_for_status()
        return json.loads(resp.text)

    def delete(self, idOrg_or_name):
        resp = requests.delete("https://trello.com/1/organizations/{}".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def delete_logo(self, idOrg_or_name):
        resp = requests.delete("https://trello.com/1/organizations/{}/logo".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def delete_member_idMember(self, idMember, idOrg_or_name):
        resp = requests.delete("https://trello.com/1/organizations/{}/members/{}".format(idOrg_or_name, idMember), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def delete_member_all_idMember(self, idMember, idOrg_or_name):
        resp = requests.delete("https://trello.com/1/organizations/{}/members/{}/all".format(idOrg_or_name, idMember), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def delete_pref_associatedDomain(self, idOrg_or_name):
        resp = requests.delete("https://trello.com/1/organizations/{}/prefs/associatedDomain".format(idOrg_or_name), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def delete_pref_orgInviteRestrict(self, idOrg_or_name, value):
        resp = requests.delete("https://trello.com/1/organizations/{}/prefs/orgInviteRestrict".format(idOrg_or_name), params={"key": self._apikey, "token": self._token, "value": value}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)


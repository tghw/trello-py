from .base import ApiBase
import requests

class Boards(ApiBase):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, board_id, actions=None, actions_entities=None, actions_display=None, actions_format=None, actions_since=None, actions_limit=None, action_fields=None, action_member=None, action_member_fields=None, action_memberCreator=None, action_memberCreator_fields=None, cards=None, card_fields=None, card_attachments=None, card_attachment_fields=None, card_checklists=None, card_pluginData=None, card_stickers=None, boardStars=None, labels=None, label_fields=None, labels_limit=None, lists=None, list_fields=None, memberships=None, memberships_member=None, memberships_member_fields=None, members=None, member_fields=None, membersInvited=None, membersInvited_fields=None, pluginData=None, checklists=None, checklist_fields=None, organization=None, organization_fields=None, organization_memberships=None, organization_pluginData=None, myPrefs=None, tags=None, fields=None):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}", params={"key": self._apikey, "token": self._token, "actions": actions, "actions_entities": actions_entities, "actions_display": actions_display, "actions_format": actions_format, "actions_since": actions_since, "actions_limit": actions_limit, "action_fields": action_fields, "action_member": action_member, "action_member_fields": action_member_fields, "action_memberCreator": action_memberCreator, "action_memberCreator_fields": action_memberCreator_fields, "cards": cards, "card_fields": card_fields, "card_attachments": card_attachments, "card_attachment_fields": card_attachment_fields, "card_checklists": card_checklists, "card_pluginData": card_pluginData, "card_stickers": card_stickers, "boardStars": boardStars, "labels": labels, "label_fields": label_fields, "labels_limit": labels_limit, "lists": lists, "list_fields": list_fields, "memberships": memberships, "memberships_member": memberships_member, "memberships_member_fields": memberships_member_fields, "members": members, "member_fields": member_fields, "membersInvited": membersInvited, "membersInvited_fields": membersInvited_fields, "pluginData": pluginData, "checklists": checklists, "checklist_fields": checklist_fields, "organization": organization, "organization_fields": organization_fields, "organization_memberships": organization_memberships, "organization_pluginData": organization_pluginData, "myPrefs": myPrefs, "tags": tags, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_field(self, field, board_id):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_action(self, board_id, entities=None, display=None, filter=None, fields=None, limit=None, format=None, since=None, before=None, page=None, idModels=None, member=None, member_fields=None, memberCreator=None, memberCreator_fields=None):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/actions", params={"key": self._apikey, "token": self._token, "entities": entities, "display": display, "filter": filter, "fields": fields, "limit": limit, "format": format, "since": since, "before": before, "page": page, "idModels": idModels, "member": member, "member_fields": member_fields, "memberCreator": memberCreator, "memberCreator_fields": memberCreator_fields}, data=None)
        return self.raise_or_json(resp)

    def get_boardStar(self, board_id, filter=None):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/boardStars", params={"key": self._apikey, "token": self._token, "filter": filter}, data=None)
        return self.raise_or_json(resp)

    def get_card(self, board_id, actions=None, attachments=None, attachment_fields=None, stickers=None, members=None, member_fields=None, checkItemStates=None, checklists=None, limit=None, since=None, before=None, filter=None, fields=None, customFieldItems=None):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/cards", params={"key": self._apikey, "token": self._token, "actions": actions, "attachments": attachments, "attachment_fields": attachment_fields, "stickers": stickers, "members": members, "member_fields": member_fields, "checkItemStates": checkItemStates, "checklists": checklists, "limit": limit, "since": since, "before": before, "filter": filter, "fields": fields, "customFieldItems": "true" if customFieldItems else None}, data=None)
        return self.raise_or_json(resp)

    def get_card_filter(self, filter, board_id):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/cards/{filter}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_card_idCard(self, idCard, board_id, attachments=None, attachment_fields=None, actions=None, actions_entities=None, actions_display=None, actions_limit=None, action_fields=None, action_memberCreator_fields=None, members=None, member_fields=None, checkItemStates=None, checkItemState_fields=None, labels=None, checklists=None, checklist_fields=None, fields=None):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/cards/{idCard}", params={"key": self._apikey, "token": self._token, "attachments": attachments, "attachment_fields": attachment_fields, "actions": actions, "actions_entities": actions_entities, "actions_display": actions_display, "actions_limit": actions_limit, "action_fields": action_fields, "action_memberCreator_fields": action_memberCreator_fields, "members": members, "member_fields": member_fields, "checkItemStates": checkItemStates, "checkItemState_fields": checkItemState_fields, "labels": labels, "checklists": checklists, "checklist_fields": checklist_fields, "fields": fields}, data=None)
        return self.raise_or_json(resp)
    
    def get_custom_fields(self, board_id):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/customFields", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_checklist(self, board_id, cards=None, card_fields=None, checkItems=None, checkItem_fields=None, filter=None, fields=None):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/checklists", params={"key": self._apikey, "token": self._token, "cards": cards, "card_fields": card_fields, "checkItems": checkItems, "checkItem_fields": checkItem_fields, "filter": filter, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_delta(self, board_id, tags, ixLastUpdate):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/deltas", params={"key": self._apikey, "token": self._token, "tags": tags, "ixLastUpdate": ixLastUpdate}, data=None)
        return self.raise_or_json(resp)

    def get_label(self, board_id, fields=None, limit=None):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/labels", params={"key": self._apikey, "token": self._token, "fields": fields, "limit": limit}, data=None)
        return self.raise_or_json(resp)

    def get_label_idLabel(self, idLabel, board_id, fields=None):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/labels/{idLabel}", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_list(self, board_id, cards=None, card_fields=None, filter=None, fields=None):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/lists", params={"key": self._apikey, "token": self._token, "cards": cards, "card_fields": card_fields, "filter": filter, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_list_filter(self, filter, board_id):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/lists/{filter}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_member(self, board_id, filter=None, fields=None, activity=None):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/members", params={"key": self._apikey, "token": self._token, "filter": filter, "fields": fields, "activity": activity}, data=None)
        return self.raise_or_json(resp)

    def get_member_filter(self, filter, board_id):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/members/{filter}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_member_card_idMember(self, idMember, board_id, actions=None, attachments=None, attachment_fields=None, members=None, member_fields=None, checkItemStates=None, checklists=None, board=None, board_fields=None, list=None, list_fields=None, filter=None, fields=None):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/members/{idMember}/cards", params={"key": self._apikey, "token": self._token, "actions": actions, "attachments": attachments, "attachment_fields": attachment_fields, "members": members, "member_fields": member_fields, "checkItemStates": checkItemStates, "checklists": checklists, "board": board, "board_fields": board_fields, "list": list, "list_fields": list_fields, "filter": filter, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_membersInvited(self, board_id, fields=None):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/membersInvited", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_membersInvited_field(self, field, board_id):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/membersInvited/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_membership(self, board_id, filter=None, member=None, member_fields=None):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/memberships", params={"key": self._apikey, "token": self._token, "filter": filter, "member": member, "member_fields": member_fields}, data=None)
        return self.raise_or_json(resp)

    def get_membership_idMembership(self, idMembership, board_id, member=None, member_fields=None):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/memberships/{idMembership}", params={"key": self._apikey, "token": self._token, "member": member, "member_fields": member_fields}, data=None)
        return self.raise_or_json(resp)

    def get_myPref(self, board_id):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/myPrefs", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_organization(self, board_id, fields=None):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/organization", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_organization_field(self, field, board_id):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/organization/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_pluginData(self, board_id):
        resp = requests.get(f"https://trello.com/1/boards/{board_id}/pluginData", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def update(self, board_id, name=None, desc=None, closed=None, subscribed=None, idOrganization=None, prefs_permissionLevel=None, prefs_selfJoin=None, prefs_cardCovers=None, prefs_invitations=None, prefs_voting=None, prefs_comments=None, prefs_background=None, prefs_cardAging=None, prefs_calendarFeedEnabled=None, labelNames_green=None, labelNames_yellow=None, labelNames_orange=None, labelNames_red=None, labelNames_purple=None, labelNames_blue=None):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}", params={"key": self._apikey, "token": self._token}, data={"name": name, "desc": desc, "closed": closed, "subscribed": subscribed, "idOrganization": idOrganization, "prefs/permissionLevel": prefs_permissionLevel, "prefs/selfJoin": prefs_selfJoin, "prefs/cardCovers": prefs_cardCovers, "prefs/invitations": prefs_invitations, "prefs/voting": prefs_voting, "prefs/comments": prefs_comments, "prefs/background": prefs_background, "prefs/cardAging": prefs_cardAging, "prefs/calendarFeedEnabled": prefs_calendarFeedEnabled, "labelNames/green": labelNames_green, "labelNames/yellow": labelNames_yellow, "labelNames/orange": labelNames_orange, "labelNames/red": labelNames_red, "labelNames/purple": labelNames_purple, "labelNames/blue": labelNames_blue})
        return self.raise_or_json(resp)

    def update_closed(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/closed", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_desc(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/desc", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_idOrganization(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/idOrganization", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_labelName_blue(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/labelNames/blue", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_labelName_green(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/labelNames/green", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_labelName_orange(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/labelNames/orange", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_labelName_purple(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/labelNames/purple", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_labelName_red(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/labelNames/red", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_labelName_yellow(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/labelNames/yellow", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_member(self, board_id, email, fullName=None, type=None):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/members", params={"key": self._apikey, "token": self._token}, data={"email": email, "fullName": fullName, "type": type})
        return self.raise_or_json(resp)

    def update_member_idMember(self, idMember, board_id, type):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/members/{idMember}", params={"key": self._apikey, "token": self._token}, data={"type": type})
        return self.raise_or_json(resp)

    def update_membership_idMembership(self, idMembership, board_id, type, member_fields=None):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/memberships/{idMembership}", params={"key": self._apikey, "token": self._token}, data={"type": type, "member_fields": member_fields})
        return self.raise_or_json(resp)

    def update_myPref_emailPosition(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/myPrefs/emailPosition", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_myPref_idEmailList(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/myPrefs/idEmailList", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_myPref_showListGuide(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/myPrefs/showListGuide", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_myPref_showSidebar(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/myPrefs/showSidebar", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_myPref_showSidebarActivity(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/myPrefs/showSidebarActivity", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_myPref_showSidebarBoardAction(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/myPrefs/showSidebarBoardActions", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_myPref_showSidebarMember(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/myPrefs/showSidebarMembers", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_name(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/name", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_pref_background(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/prefs/background", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_pref_calendarFeedEnabled(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/prefs/calendarFeedEnabled", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_pref_cardAging(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/prefs/cardAging", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_pref_cardCover(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/prefs/cardCovers", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_pref_comment(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/prefs/comments", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_pref_invitation(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/prefs/invitations", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_pref_permissionLevel(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/prefs/permissionLevel", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_pref_selfJoin(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/prefs/selfJoin", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_pref_voting(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/prefs/voting", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_subscribed(self, board_id, value):
        resp = requests.put(f"https://trello.com/1/boards/{board_id}/subscribed", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def new(self, name, defaultLabels=None, defaultLists=None, desc=None, idOrganization=None, idBoardSource=None, keepFromSource=None, powerUps=None, prefs_permissionLevel=None, prefs_voting=None, prefs_comments=None, prefs_invitations=None, prefs_selfJoin=None, prefs_cardCovers=None, prefs_background=None, prefs_cardAging=None):
        resp = requests.post("https://trello.com/1/boards", params={"key": self._apikey, "token": self._token}, data={"name": name, "defaultLabels": defaultLabels, "defaultLists": defaultLists, "desc": desc, "idOrganization": idOrganization, "idBoardSource": idBoardSource, "keepFromSource": keepFromSource, "powerUps": powerUps, "prefs_permissionLevel": prefs_permissionLevel, "prefs_voting": prefs_voting, "prefs_comments": prefs_comments, "prefs_invitations": prefs_invitations, "prefs_selfJoin": prefs_selfJoin, "prefs_cardCovers": prefs_cardCovers, "prefs_background": prefs_background, "prefs_cardAging": prefs_cardAging})
        return self.raise_or_json(resp)

    def new_calendarKey_generate(self, board_id):
        resp = requests.post(f"https://trello.com/1/boards/{board_id}/calendarKey/generate", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def new_checklist(self, board_id, name):
        resp = requests.post(f"https://trello.com/1/boards/{board_id}/checklists", params={"key": self._apikey, "token": self._token}, data={"name": name})
        return self.raise_or_json(resp)

    def new_emailKey_generate(self, board_id):
        resp = requests.post(f"https://trello.com/1/boards/{board_id}/emailKey/generate", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def new_label(self, board_id, name, color):
        resp = requests.post(f"https://trello.com/1/boards/{board_id}/labels", params={"key": self._apikey, "token": self._token}, data={"name": name, "color": color})
        return self.raise_or_json(resp)

    def new_list(self, board_id, name, pos=None):
        resp = requests.post(f"https://trello.com/1/boards/{board_id}/lists", params={"key": self._apikey, "token": self._token}, data={"name": name, "pos": pos})
        return self.raise_or_json(resp)

    def new_markAsViewed(self, board_id):
        resp = requests.post(f"https://trello.com/1/boards/{board_id}/markAsViewed", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def new_powerUp(self, board_id, value):
        resp = requests.post(f"https://trello.com/1/boards/{board_id}/powerUps", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def delete_member_idMember(self, idMember, board_id):
        resp = requests.delete(f"https://trello.com/1/boards/{board_id}/members/{idMember}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def delete_powerUp_powerUp(self, powerUp, board_id):
        resp = requests.delete(f"https://trello.com/1/boards/{board_id}/powerUps/{powerUp}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)


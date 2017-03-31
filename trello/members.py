import json
import requests

class Members(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idMember_or_username, actions=None, actions_entities=None, actions_display=None, actions_limit=None, action_fields=None, action_since=None, action_before=None, cards=None, card_fields=None, card_members=None, card_member_fields=None, card_attachments=None, card_attachment_fields=None, card_stickers=None, boards=None, board_fields=None, board_actions=None, board_actions_entities=None, board_actions_display=None, board_actions_format=None, board_actions_since=None, board_actions_limit=None, board_action_fields=None, board_lists=None, board_memberships=None, board_organization=None, board_organization_fields=None, boardsInvited=None, boardsInvited_fields=None, boardStars=None, savedSearches=None, organizations=None, organization_fields=None, organization_paid_account=None, organizationsInvited=None, organizationsInvited_fields=None, notifications=None, notifications_entities=None, notifications_display=None, notifications_limit=None, notification_fields=None, notification_memberCreator=None, notification_memberCreator_fields=None, notification_before=None, notification_since=None, tokens=None, paid_account=None, boardBackgrounds=None, customBoardBackgrounds=None, customStickers=None, customEmoji=None, fields=None):
        resp = requests.get("https://trello.com/1/members/{}".format(idMember_or_username), params={"key": self._apikey, "token": self._token, "actions": actions, "actions_entities": actions_entities, "actions_display": actions_display, "actions_limit": actions_limit, "action_fields": action_fields, "action_since": action_since, "action_before": action_before, "cards": cards, "card_fields": card_fields, "card_members": card_members, "card_member_fields": card_member_fields, "card_attachments": card_attachments, "card_attachment_fields": card_attachment_fields, "card_stickers": card_stickers, "boards": boards, "board_fields": board_fields, "board_actions": board_actions, "board_actions_entities": board_actions_entities, "board_actions_display": board_actions_display, "board_actions_format": board_actions_format, "board_actions_since": board_actions_since, "board_actions_limit": board_actions_limit, "board_action_fields": board_action_fields, "board_lists": board_lists, "board_memberships": board_memberships, "board_organization": board_organization, "board_organization_fields": board_organization_fields, "boardsInvited": boardsInvited, "boardsInvited_fields": boardsInvited_fields, "boardStars": boardStars, "savedSearches": savedSearches, "organizations": organizations, "organization_fields": organization_fields, "organization_paid_account": organization_paid_account, "organizationsInvited": organizationsInvited, "organizationsInvited_fields": organizationsInvited_fields, "notifications": notifications, "notifications_entities": notifications_entities, "notifications_display": notifications_display, "notifications_limit": notifications_limit, "notification_fields": notification_fields, "notification_memberCreator": notification_memberCreator, "notification_memberCreator_fields": notification_memberCreator_fields, "notification_before": notification_before, "notification_since": notification_since, "tokens": tokens, "paid_account": paid_account, "boardBackgrounds": boardBackgrounds, "customBoardBackgrounds": customBoardBackgrounds, "customStickers": customStickers, "customEmoji": customEmoji, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_field(self, field, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/{}/{}".format(idMember_or_username, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_action(self, idMember_or_username, entities=None, display=None, filter=None, fields=None, limit=None, format=None, since=None, before=None, page=None, idModels=None, member=None, member_fields=None, memberCreator=None, memberCreator_fields=None):
        resp = requests.get("https://trello.com/1/members/{}/actions".format(idMember_or_username), params={"key": self._apikey, "token": self._token, "entities": entities, "display": display, "filter": filter, "fields": fields, "limit": limit, "format": format, "since": since, "before": before, "page": page, "idModels": idModels, "member": member, "member_fields": member_fields, "memberCreator": memberCreator, "memberCreator_fields": memberCreator_fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_boardBackground(self, idMember_or_username, filter=None):
        resp = requests.get("https://trello.com/1/members/{}/boardBackgrounds".format(idMember_or_username), params={"key": self._apikey, "token": self._token, "filter": filter}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_boardBackground_idBoardBackground(self, idBoardBackground, idMember_or_username, fields=None):
        resp = requests.get("https://trello.com/1/members/{}/boardBackgrounds/{}".format(idMember_or_username, idBoardBackground), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_boardStar(self, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/{}/boardStars".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_boardStar_idBoardStar(self, idBoardStar, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/{}/boardStars/{}".format(idMember_or_username, idBoardStar), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_board(self, idMember_or_username, filter=None, fields=None, actions=None, actions_entities=None, actions_limit=None, actions_format=None, actions_since=None, action_fields=None, memberships=None, organization=None, organization_fields=None, lists=None):
        resp = requests.get("https://trello.com/1/members/{}/boards".format(idMember_or_username), params={"key": self._apikey, "token": self._token, "filter": filter, "fields": fields, "actions": actions, "actions_entities": actions_entities, "actions_limit": actions_limit, "actions_format": actions_format, "actions_since": actions_since, "action_fields": action_fields, "memberships": memberships, "organization": organization, "organization_fields": organization_fields, "lists": lists}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_board_filter(self, filter, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/{}/boards/{}".format(idMember_or_username, filter), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_boardsInvited(self, idMember_or_username, fields=None):
        resp = requests.get("https://trello.com/1/members/{}/boardsInvited".format(idMember_or_username), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_boardsInvited_field(self, field, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/{}/boardsInvited/{}".format(idMember_or_username, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_card(self, idMember_or_username, actions=None, attachments=None, attachment_fields=None, stickers=None, members=None, member_fields=None, checkItemStates=None, checklists=None, limit=None, since=None, before=None, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/members/{}/cards".format(idMember_or_username), params={"key": self._apikey, "token": self._token, "actions": actions, "attachments": attachments, "attachment_fields": attachment_fields, "stickers": stickers, "members": members, "member_fields": member_fields, "checkItemStates": checkItemStates, "checklists": checklists, "limit": limit, "since": since, "before": before, "filter": filter, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_card_filter(self, filter, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/{}/cards/{}".format(idMember_or_username, filter), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_customBoardBackground(self, idMember_or_username, filter=None):
        resp = requests.get("https://trello.com/1/members/{}/customBoardBackgrounds".format(idMember_or_username), params={"key": self._apikey, "token": self._token, "filter": filter}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_customBoardBackground_idBoardBackground(self, idBoardBackground, idMember_or_username, fields=None):
        resp = requests.get("https://trello.com/1/members/{}/customBoardBackgrounds/{}".format(idMember_or_username, idBoardBackground), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_customEmoji(self, idMember_or_username, filter=None):
        resp = requests.get("https://trello.com/1/members/{}/customEmoji".format(idMember_or_username), params={"key": self._apikey, "token": self._token, "filter": filter}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_customEmoji_idCustomEmoji(self, idCustomEmoji, idMember_or_username, fields=None):
        resp = requests.get("https://trello.com/1/members/{}/customEmoji/{}".format(idMember_or_username, idCustomEmoji), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_customSticker(self, idMember_or_username, filter=None):
        resp = requests.get("https://trello.com/1/members/{}/customStickers".format(idMember_or_username), params={"key": self._apikey, "token": self._token, "filter": filter}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_customSticker_idCustomSticker(self, idCustomSticker, idMember_or_username, fields=None):
        resp = requests.get("https://trello.com/1/members/{}/customStickers/{}".format(idMember_or_username, idCustomSticker), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_delta(self, idMember_or_username, tags, ixLastUpdate):
        resp = requests.get("https://trello.com/1/members/{}/deltas".format(idMember_or_username), params={"key": self._apikey, "token": self._token, "tags": tags, "ixLastUpdate": ixLastUpdate}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_notification(self, idMember_or_username, entities=None, display=None, filter=None, read_filter=None, fields=None, limit=None, page=None, before=None, since=None, memberCreator=None, memberCreator_fields=None):
        resp = requests.get("https://trello.com/1/members/{}/notifications".format(idMember_or_username), params={"key": self._apikey, "token": self._token, "entities": entities, "display": display, "filter": filter, "read_filter": read_filter, "fields": fields, "limit": limit, "page": page, "before": before, "since": since, "memberCreator": memberCreator, "memberCreator_fields": memberCreator_fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_notification_filter(self, filter, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/{}/notifications/{}".format(idMember_or_username, filter), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_organization(self, idMember_or_username, filter=None, fields=None, paid_account=None):
        resp = requests.get("https://trello.com/1/members/{}/organizations".format(idMember_or_username), params={"key": self._apikey, "token": self._token, "filter": filter, "fields": fields, "paid_account": paid_account}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_organization_filter(self, filter, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/{}/organizations/{}".format(idMember_or_username, filter), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_organizationsInvited(self, idMember_or_username, fields=None):
        resp = requests.get("https://trello.com/1/members/{}/organizationsInvited".format(idMember_or_username), params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_organizationsInvited_field(self, field, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/{}/organizationsInvited/{}".format(idMember_or_username, field), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_savedSearche(self, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/{}/savedSearches".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_savedSearche_idSavedSearch(self, idSavedSearch, idMember_or_username):
        resp = requests.get("https://trello.com/1/members/{}/savedSearches/{}".format(idMember_or_username, idSavedSearch), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_token(self, idMember_or_username, filter=None, webhooks=None):
        resp = requests.get("https://trello.com/1/members/{}/tokens".format(idMember_or_username), params={"key": self._apikey, "token": self._token, "filter": filter, "webhooks": webhooks}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def update(self, idMember_or_username, fullName=None, initials=None, username=None, bio=None, avatarSource=None, prefs_colorBlind=None, prefs_locale=None, prefs_minutesBetweenSummaries=None):
        resp = requests.put("https://trello.com/1/members/{}".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"fullName": fullName, "initials": initials, "username": username, "bio": bio, "avatarSource": avatarSource, "prefs/colorBlind": prefs_colorBlind, "prefs/locale": prefs_locale, "prefs/minutesBetweenSummaries": prefs_minutesBetweenSummaries})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_avatarSource(self, idMember_or_username, value):
        resp = requests.put("https://trello.com/1/members/{}/avatarSource".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_bio(self, idMember_or_username, value):
        resp = requests.put("https://trello.com/1/members/{}/bio".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_boardBackground_idBoardBackground(self, idBoardBackground, idMember_or_username, tile=None, brightness=None):
        resp = requests.put("https://trello.com/1/members/{}/boardBackgrounds/{}".format(idMember_or_username, idBoardBackground), params={"key": self._apikey, "token": self._token}, data={"tile": tile, "brightness": brightness})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_boardStar(self, idMember_or_username, idBoard=None, pos=None):
        resp = requests.put("https://trello.com/1/members/{}/boardStars/{}".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"idBoard": idBoard, "pos": pos})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_boardStar_idBoard_idBoardStar(self, idBoardStar, idMember_or_username, value):
        resp = requests.put("https://trello.com/1/members/{}/boardStars/{}/idBoard".format(idMember_or_username, idBoardStar), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_boardStar_po_idBoardStar(self, idBoardStar, idMember_or_username, value):
        resp = requests.put("https://trello.com/1/members/{}/boardStars/{}/pos".format(idMember_or_username, idBoardStar), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_customBoardBackground_idBoardBackground(self, idBoardBackground, idMember_or_username, tile=None, brightness=None):
        resp = requests.put("https://trello.com/1/members/{}/customBoardBackgrounds/{}".format(idMember_or_username, idBoardBackground), params={"key": self._apikey, "token": self._token}, data={"tile": tile, "brightness": brightness})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_fullName(self, idMember_or_username, value):
        resp = requests.put("https://trello.com/1/members/{}/fullName".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_initial(self, idMember_or_username, value):
        resp = requests.put("https://trello.com/1/members/{}/initials".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_pref_colorBlind(self, idMember_or_username, value):
        resp = requests.put("https://trello.com/1/members/{}/prefs/colorBlind".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_pref_locale(self, idMember_or_username, value):
        resp = requests.put("https://trello.com/1/members/{}/prefs/locale".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_pref_minutesBetweenSummarie(self, idMember_or_username, value):
        resp = requests.put("https://trello.com/1/members/{}/prefs/minutesBetweenSummaries".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_savedSearche(self, idMember_or_username, name=None, query=None, pos=None):
        resp = requests.put("https://trello.com/1/members/{}/savedSearches/{}".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"name": name, "query": query, "pos": pos})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_savedSearche_name_idSavedSearch(self, idSavedSearch, idMember_or_username, value):
        resp = requests.put("https://trello.com/1/members/{}/savedSearches/{}/name".format(idMember_or_username, idSavedSearch), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_savedSearche_po_idSavedSearch(self, idSavedSearch, idMember_or_username, value):
        resp = requests.put("https://trello.com/1/members/{}/savedSearches/{}/pos".format(idMember_or_username, idSavedSearch), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_savedSearche_query_idSavedSearch(self, idSavedSearch, idMember_or_username, value):
        resp = requests.put("https://trello.com/1/members/{}/savedSearches/{}/query".format(idMember_or_username, idSavedSearch), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def update_username(self, idMember_or_username, value):
        resp = requests.put("https://trello.com/1/members/{}/username".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def new_avatar(self, idMember_or_username, file):
        resp = requests.post("https://trello.com/1/members/{}/avatar".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"file": file})
        resp.raise_for_status()
        return json.loads(resp.text)

    def new_boardBackground(self, idMember_or_username, file):
        resp = requests.post("https://trello.com/1/members/{}/boardBackgrounds".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"file": file})
        resp.raise_for_status()
        return json.loads(resp.text)

    def new_boardStar(self, idMember_or_username, idBoard, pos):
        resp = requests.post("https://trello.com/1/members/{}/boardStars".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"idBoard": idBoard, "pos": pos})
        resp.raise_for_status()
        return json.loads(resp.text)

    def new_customBoardBackground(self, idMember_or_username, file):
        resp = requests.post("https://trello.com/1/members/{}/customBoardBackgrounds".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"file": file})
        resp.raise_for_status()
        return json.loads(resp.text)

    def new_customEmoji(self, idMember_or_username, file, name):
        resp = requests.post("https://trello.com/1/members/{}/customEmoji".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"file": file, "name": name})
        resp.raise_for_status()
        return json.loads(resp.text)

    def new_customSticker(self, idMember_or_username, file):
        resp = requests.post("https://trello.com/1/members/{}/customStickers".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"file": file})
        resp.raise_for_status()
        return json.loads(resp.text)

    def new_oneTimeMessagesDismissed(self, idMember_or_username, value):
        resp = requests.post("https://trello.com/1/members/{}/oneTimeMessagesDismissed".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"value": value})
        resp.raise_for_status()
        return json.loads(resp.text)

    def new_savedSearche(self, idMember_or_username, name, query, pos):
        resp = requests.post("https://trello.com/1/members/{}/savedSearches".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"name": name, "query": query, "pos": pos})
        resp.raise_for_status()
        return json.loads(resp.text)

    def delete_boardBackground_idBoardBackground(self, idBoardBackground, idMember_or_username):
        resp = requests.delete("https://trello.com/1/members/{}/boardBackgrounds/{}".format(idMember_or_username, idBoardBackground), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def delete_boardStar_idBoardStar(self, idBoardStar, idMember_or_username):
        resp = requests.delete("https://trello.com/1/members/{}/boardStars/{}".format(idMember_or_username, idBoardStar), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def delete_customBoardBackground_idBoardBackground(self, idBoardBackground, idMember_or_username):
        resp = requests.delete("https://trello.com/1/members/{}/customBoardBackgrounds/{}".format(idMember_or_username, idBoardBackground), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def delete_customSticker_idCustomSticker(self, idCustomSticker, idMember_or_username):
        resp = requests.delete("https://trello.com/1/members/{}/customStickers/{}".format(idMember_or_username, idCustomSticker), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def delete_savedSearche_idSavedSearch(self, idSavedSearch, idMember_or_username):
        resp = requests.delete("https://trello.com/1/members/{}/savedSearches/{}".format(idMember_or_username, idSavedSearch), params={"key": self._apikey, "token": self._token}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)


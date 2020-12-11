from .base import ApiBase
import requests

class Members(ApiBase):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, idMember_or_username, actions=None, actions_entities=None, actions_display=None, actions_limit=None, action_fields=None, action_since=None, action_before=None, cards=None, card_fields=None, card_members=None, card_member_fields=None, card_attachments=None, card_attachment_fields=None, card_stickers=None, boards=None, board_fields=None, board_actions=None, board_actions_entities=None, board_actions_display=None, board_actions_format=None, board_actions_since=None, board_actions_limit=None, board_action_fields=None, board_lists=None, board_memberships=None, board_organization=None, board_organization_fields=None, boardsInvited=None, boardsInvited_fields=None, boardStars=None, savedSearches=None, organizations=None, organization_fields=None, organization_paid_account=None, organizationsInvited=None, organizationsInvited_fields=None, notifications=None, notifications_entities=None, notifications_display=None, notifications_limit=None, notification_fields=None, notification_memberCreator=None, notification_memberCreator_fields=None, notification_before=None, notification_since=None, tokens=None, paid_account=None, boardBackgrounds=None, customBoardBackgrounds=None, customStickers=None, customEmoji=None, fields=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}", params={"key": self._apikey, "token": self._token, "actions": actions, "actions_entities": actions_entities, "actions_display": actions_display, "actions_limit": actions_limit, "action_fields": action_fields, "action_since": action_since, "action_before": action_before, "cards": cards, "card_fields": card_fields, "card_members": card_members, "card_member_fields": card_member_fields, "card_attachments": card_attachments, "card_attachment_fields": card_attachment_fields, "card_stickers": card_stickers, "boards": boards, "board_fields": board_fields, "board_actions": board_actions, "board_actions_entities": board_actions_entities, "board_actions_display": board_actions_display, "board_actions_format": board_actions_format, "board_actions_since": board_actions_since, "board_actions_limit": board_actions_limit, "board_action_fields": board_action_fields, "board_lists": board_lists, "board_memberships": board_memberships, "board_organization": board_organization, "board_organization_fields": board_organization_fields, "boardsInvited": boardsInvited, "boardsInvited_fields": boardsInvited_fields, "boardStars": boardStars, "savedSearches": savedSearches, "organizations": organizations, "organization_fields": organization_fields, "organization_paid_account": organization_paid_account, "organizationsInvited": organizationsInvited, "organizationsInvited_fields": organizationsInvited_fields, "notifications": notifications, "notifications_entities": notifications_entities, "notifications_display": notifications_display, "notifications_limit": notifications_limit, "notification_fields": notification_fields, "notification_memberCreator": notification_memberCreator, "notification_memberCreator_fields": notification_memberCreator_fields, "notification_before": notification_before, "notification_since": notification_since, "tokens": tokens, "paid_account": paid_account, "boardBackgrounds": boardBackgrounds, "customBoardBackgrounds": customBoardBackgrounds, "customStickers": customStickers, "customEmoji": customEmoji, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_field(self, field, idMember_or_username):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_action(self, idMember_or_username, entities=None, display=None, filter=None, fields=None, limit=None, format=None, since=None, before=None, page=None, idModels=None, member=None, member_fields=None, memberCreator=None, memberCreator_fields=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/actions", params={"key": self._apikey, "token": self._token, "entities": entities, "display": display, "filter": filter, "fields": fields, "limit": limit, "format": format, "since": since, "before": before, "page": page, "idModels": idModels, "member": member, "member_fields": member_fields, "memberCreator": memberCreator, "memberCreator_fields": memberCreator_fields}, data=None)
        return self.raise_or_json(resp)

    def get_boardBackground(self, idMember_or_username, filter=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/boardBackgrounds", params={"key": self._apikey, "token": self._token, "filter": filter}, data=None)
        return self.raise_or_json(resp)

    def get_boardBackground_idBoardBackground(self, idBoardBackground, idMember_or_username, fields=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/boardBackgrounds/{idBoardBackground}", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_boardStar(self, idMember_or_username):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/boardStars", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_boardStar_idBoardStar(self, idBoardStar, idMember_or_username):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/boardStars/{idBoardStar}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_board(self, idMember_or_username, filter=None, fields=None, actions=None, actions_entities=None, actions_limit=None, actions_format=None, actions_since=None, action_fields=None, memberships=None, organization=None, organization_fields=None, lists=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/boards", params={"key": self._apikey, "token": self._token, "filter": filter, "fields": fields, "actions": actions, "actions_entities": actions_entities, "actions_limit": actions_limit, "actions_format": actions_format, "actions_since": actions_since, "action_fields": action_fields, "memberships": memberships, "organization": organization, "organization_fields": organization_fields, "lists": lists}, data=None)
        return self.raise_or_json(resp)

    def get_board_filter(self, filter, idMember_or_username):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/boards/{filter}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_boardsInvited(self, idMember_or_username, fields=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/boardsInvited", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_boardsInvited_field(self, field, idMember_or_username):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/boardsInvited/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_card(self, idMember_or_username, actions=None, attachments=None, attachment_fields=None, stickers=None, members=None, member_fields=None, checkItemStates=None, checklists=None, limit=None, since=None, before=None, filter=None, fields=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/cards", params={"key": self._apikey, "token": self._token, "actions": actions, "attachments": attachments, "attachment_fields": attachment_fields, "stickers": stickers, "members": members, "member_fields": member_fields, "checkItemStates": checkItemStates, "checklists": checklists, "limit": limit, "since": since, "before": before, "filter": filter, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_card_filter(self, filter, idMember_or_username):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/cards/{filter}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_customBoardBackground(self, idMember_or_username, filter=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/customBoardBackgrounds", params={"key": self._apikey, "token": self._token, "filter": filter}, data=None)
        return self.raise_or_json(resp)

    def get_customBoardBackground_idBoardBackground(self, idBoardBackground, idMember_or_username, fields=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/customBoardBackgrounds/{idBoardBackground}", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_customEmoji(self, idMember_or_username, filter=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/customEmoji", params={"key": self._apikey, "token": self._token, "filter": filter}, data=None)
        return self.raise_or_json(resp)

    def get_customEmoji_idCustomEmoji(self, idCustomEmoji, idMember_or_username, fields=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/customEmoji/{idCustomEmoji}", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_customSticker(self, idMember_or_username, filter=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/customStickers", params={"key": self._apikey, "token": self._token, "filter": filter}, data=None)
        return self.raise_or_json(resp)

    def get_customSticker_idCustomSticker(self, idCustomSticker, idMember_or_username, fields=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/customStickers/{idCustomSticker}", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_delta(self, idMember_or_username, tags, ixLastUpdate):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/deltas", params={"key": self._apikey, "token": self._token, "tags": tags, "ixLastUpdate": ixLastUpdate}, data=None)
        return self.raise_or_json(resp)

    def get_notification(self, idMember_or_username, entities=None, display=None, filter=None, read_filter=None, fields=None, limit=None, page=None, before=None, since=None, memberCreator=None, memberCreator_fields=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/notifications", params={"key": self._apikey, "token": self._token, "entities": entities, "display": display, "filter": filter, "read_filter": read_filter, "fields": fields, "limit": limit, "page": page, "before": before, "since": since, "memberCreator": memberCreator, "memberCreator_fields": memberCreator_fields}, data=None)
        return self.raise_or_json(resp)

    def get_notification_filter(self, filter, idMember_or_username):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/notifications/{filter}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_organization(self, idMember_or_username, filter=None, fields=None, paid_account=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/organizations", params={"key": self._apikey, "token": self._token, "filter": filter, "fields": fields, "paid_account": paid_account}, data=None)
        return self.raise_or_json(resp)

    def get_organization_filter(self, filter, idMember_or_username):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/organizations/{filter}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_organizationsInvited(self, idMember_or_username, fields=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/organizationsInvited", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_organizationsInvited_field(self, field, idMember_or_username):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/organizationsInvited/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_savedSearche(self, idMember_or_username):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/savedSearches", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_savedSearche_idSavedSearch(self, idSavedSearch, idMember_or_username):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/savedSearches/{idSavedSearch}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_token(self, idMember_or_username, filter=None, webhooks=None):
        resp = requests.get(f"https://trello.com/1/members/{idMember_or_username}/tokens", params={"key": self._apikey, "token": self._token, "filter": filter, "webhooks": webhooks}, data=None)
        return self.raise_or_json(resp)

    def update(self, idMember_or_username, fullName=None, initials=None, username=None, bio=None, avatarSource=None, prefs_colorBlind=None, prefs_locale=None, prefs_minutesBetweenSummaries=None):
        resp = requests.put(f"https://trello.com/1/members/{idMember_or_username}", params={"key": self._apikey, "token": self._token}, data={"fullName": fullName, "initials": initials, "username": username, "bio": bio, "avatarSource": avatarSource, "prefs/colorBlind": prefs_colorBlind, "prefs/locale": prefs_locale, "prefs/minutesBetweenSummaries": prefs_minutesBetweenSummaries})
        return self.raise_or_json(resp)

    def update_avatarSource(self, idMember_or_username, value):
        resp = requests.put(f"https://trello.com/1/members/{idMember_or_username}/avatarSource", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_bio(self, idMember_or_username, value):
        resp = requests.put(f"https://trello.com/1/members/{idMember_or_username}/bio", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_boardBackground_idBoardBackground(self, idBoardBackground, idMember_or_username, tile=None, brightness=None):
        resp = requests.put(f"https://trello.com/1/members/{idMember_or_username}/boardBackgrounds/{idBoardBackground}", params={"key": self._apikey, "token": self._token}, data={"tile": tile, "brightness": brightness})
        return self.raise_or_json(resp)

    def update_boardStar(self, idMember_or_username, idBoard=None, pos=None):
        resp = requests.put("https://trello.com/1/members/{}/boardStars/{}".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"idBoard": idBoard, "pos": pos})
        return self.raise_or_json(resp)

    def update_boardStar_idBoard_idBoardStar(self, idBoardStar, idMember_or_username, value):
        resp = requests.put(f"https://trello.com/1/members/{idMember_or_username}/boardStars/{idBoardStar}/idBoard", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_boardStar_po_idBoardStar(self, idBoardStar, idMember_or_username, value):
        resp = requests.put(f"https://trello.com/1/members/{idMember_or_username}/boardStars/{idBoardStar}/pos", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_customBoardBackground_idBoardBackground(self, idBoardBackground, idMember_or_username, tile=None, brightness=None):
        resp = requests.put(f"https://trello.com/1/members/{idMember_or_username}/customBoardBackgrounds/{idBoardBackground}", params={"key": self._apikey, "token": self._token}, data={"tile": tile, "brightness": brightness})
        return self.raise_or_json(resp)

    def update_fullName(self, idMember_or_username, value):
        resp = requests.put(f"https://trello.com/1/members/{idMember_or_username}/fullName", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_initial(self, idMember_or_username, value):
        resp = requests.put(f"https://trello.com/1/members/{idMember_or_username}/initials", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_pref_colorBlind(self, idMember_or_username, value):
        resp = requests.put(f"https://trello.com/1/members/{idMember_or_username}/prefs/colorBlind", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_pref_locale(self, idMember_or_username, value):
        resp = requests.put(f"https://trello.com/1/members/{idMember_or_username}/prefs/locale", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_pref_minutesBetweenSummarie(self, idMember_or_username, value):
        resp = requests.put(f"https://trello.com/1/members/{idMember_or_username}/prefs/minutesBetweenSummaries", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_savedSearche(self, idMember_or_username, name=None, query=None, pos=None):
        resp = requests.put("https://trello.com/1/members/{}/savedSearches/{}".format(idMember_or_username), params={"key": self._apikey, "token": self._token}, data={"name": name, "query": query, "pos": pos})
        return self.raise_or_json(resp)

    def update_savedSearche_name_idSavedSearch(self, idSavedSearch, idMember_or_username, value):
        resp = requests.put(f"https://trello.com/1/members/{idMember_or_username}/savedSearches/{idSavedSearch}/name", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_savedSearche_po_idSavedSearch(self, idSavedSearch, idMember_or_username, value):
        resp = requests.put(f"https://trello.com/1/members/{idMember_or_username}/savedSearches/{idSavedSearch}/pos", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_savedSearche_query_idSavedSearch(self, idSavedSearch, idMember_or_username, value):
        resp = requests.put(f"https://trello.com/1/members/{idMember_or_username}/savedSearches/{idSavedSearch}/query", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_username(self, idMember_or_username, value):
        resp = requests.put(f"https://trello.com/1/members/{idMember_or_username}/username", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def new_avatar(self, idMember_or_username, file):
        resp = requests.post(f"https://trello.com/1/members/{idMember_or_username}/avatar", params={"key": self._apikey, "token": self._token}, data={"file": file})
        return self.raise_or_json(resp)

    def new_boardBackground(self, idMember_or_username, file):
        resp = requests.post(f"https://trello.com/1/members/{idMember_or_username}/boardBackgrounds", params={"key": self._apikey, "token": self._token}, data={"file": file})
        return self.raise_or_json(resp)

    def new_boardStar(self, idMember_or_username, idBoard, pos):
        resp = requests.post(f"https://trello.com/1/members/{idMember_or_username}/boardStars", params={"key": self._apikey, "token": self._token}, data={"idBoard": idBoard, "pos": pos})
        return self.raise_or_json(resp)

    def new_customBoardBackground(self, idMember_or_username, file):
        resp = requests.post(f"https://trello.com/1/members/{idMember_or_username}/customBoardBackgrounds", params={"key": self._apikey, "token": self._token}, data={"file": file})
        return self.raise_or_json(resp)

    def new_customEmoji(self, idMember_or_username, file, name):
        resp = requests.post(f"https://trello.com/1/members/{idMember_or_username}/customEmoji", params={"key": self._apikey, "token": self._token}, data={"file": file, "name": name})
        return self.raise_or_json(resp)

    def new_customSticker(self, idMember_or_username, file):
        resp = requests.post(f"https://trello.com/1/members/{idMember_or_username}/customStickers", params={"key": self._apikey, "token": self._token}, data={"file": file})
        return self.raise_or_json(resp)

    def new_oneTimeMessagesDismissed(self, idMember_or_username, value):
        resp = requests.post(f"https://trello.com/1/members/{idMember_or_username}/oneTimeMessagesDismissed", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def new_savedSearche(self, idMember_or_username, name, query, pos):
        resp = requests.post(f"https://trello.com/1/members/{idMember_or_username}/savedSearches", params={"key": self._apikey, "token": self._token}, data={"name": name, "query": query, "pos": pos})
        return self.raise_or_json(resp)

    def delete_boardBackground_idBoardBackground(self, idBoardBackground, idMember_or_username):
        resp = requests.delete(f"https://trello.com/1/members/{idMember_or_username}/boardBackgrounds/{idBoardBackground}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def delete_boardStar_idBoardStar(self, idBoardStar, idMember_or_username):
        resp = requests.delete(f"https://trello.com/1/members/{idMember_or_username}/boardStars/{idBoardStar}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def delete_customBoardBackground_idBoardBackground(self, idBoardBackground, idMember_or_username):
        resp = requests.delete(f"https://trello.com/1/members/{idMember_or_username}/customBoardBackgrounds/{idBoardBackground}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def delete_customSticker_idCustomSticker(self, idCustomSticker, idMember_or_username):
        resp = requests.delete(f"https://trello.com/1/members/{idMember_or_username}/customStickers/{idCustomSticker}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def delete_savedSearche_idSavedSearch(self, idSavedSearch, idMember_or_username):
        resp = requests.delete(f"https://trello.com/1/members/{idMember_or_username}/savedSearches/{idSavedSearch}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)


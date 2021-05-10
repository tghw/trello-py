from .base import ApiBase
import requests

class Cards(ApiBase):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, card_id_or_shortlink, actions=None, actions_entities=None, actions_display=None, actions_limit=None, action_fields=None, action_memberCreator_fields=None, attachments=None, attachment_fields=None, members=None, member_fields=None, membersVoted=None, memberVoted_fields=None, checkItemStates=None, checkItemState_fields=None, checklists=None, checklist_fields=None, board=None, board_fields=None, list=None, list_fields=None, pluginData=None, stickers=None, sticker_fields=None, fields=None):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}", params={"key": self._apikey, "token": self._token, "actions": actions, "actions_entities": actions_entities, "actions_display": actions_display, "actions_limit": actions_limit, "action_fields": action_fields, "action_memberCreator_fields": action_memberCreator_fields, "attachments": attachments, "attachment_fields": attachment_fields, "members": members, "member_fields": member_fields, "membersVoted": membersVoted, "memberVoted_fields": memberVoted_fields, "checkItemStates": checkItemStates, "checkItemState_fields": checkItemState_fields, "checklists": checklists, "checklist_fields": checklist_fields, "board": board, "board_fields": board_fields, "list": list, "list_fields": list_fields, "pluginData": pluginData, "stickers": stickers, "sticker_fields": sticker_fields, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_field(self, field, card_id_or_shortlink):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_action(self, card_id_or_shortlink, entities=None, display=None, filter=None, fields=None, limit=None, format=None, since=None, before=None, idModels=None, member=None, member_fields=None, memberCreator=None, memberCreator_fields=None):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}/actions", params={"key": self._apikey, "token": self._token, "entities": entities, "display": display, "filter": filter, "fields": fields, "limit": limit, "format": format, "since": since, "before": before, "idModels": idModels, "member": member, "member_fields": member_fields, "memberCreator": memberCreator, "memberCreator_fields": memberCreator_fields}, data=None)
        return self.raise_or_json(resp)

    def get_attachment(self, card_id_or_shortlink, fields=None, filter=None):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}/attachments", params={"key": self._apikey, "token": self._token, "fields": fields, "filter": filter}, data=None)
        return self.raise_or_json(resp)

    def get_attachment_idAttachment(self, idAttachment, card_id_or_shortlink, fields=None):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}/attachments/{idAttachment}", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_board(self, card_id_or_shortlink, fields=None):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}/board", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_board_field(self, field, card_id_or_shortlink):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}/board/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_checkItemState(self, card_id_or_shortlink, fields=None):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}/checkItemStates", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_checklist(self, card_id_or_shortlink, cards=None, card_fields=None, checkItems=None, checkItem_fields=None, filter=None, fields=None):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}/checklists", params={"key": self._apikey, "token": self._token, "cards": cards, "card_fields": card_fields, "checkItems": checkItems, "checkItem_fields": checkItem_fields, "filter": filter, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_checkItem_idCheckItem(self, idCheckItem, card_id_or_shortlink, fields=None):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}/checkItem/{idCheckItem}", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_list(self, card_id_or_shortlink, fields=None):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}/list", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_list_field(self, field, card_id_or_shortlink):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}/list/{field}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_member(self, card_id_or_shortlink, fields=None):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}/members", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_membersVoted(self, card_id_or_shortlink, fields=None):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}/membersVoted", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_pluginData(self, card_id_or_shortlink):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}/pluginData", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def get_sticker(self, card_id_or_shortlink, fields=None):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}/stickers", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def get_sticker_idSticker(self, idSticker, card_id_or_shortlink, fields=None):
        resp = requests.get(f"https://trello.com/1/cards/{card_id_or_shortlink}/stickers/{idSticker}", params={"key": self._apikey, "token": self._token, "fields": fields}, data=None)
        return self.raise_or_json(resp)

    def update(self, card_id_or_shortlink, name=None, desc=None, closed=None, idMembers=None, idAttachmentCover=None, idList=None, idLabels=None, idBoard=None, pos=None, due=None, dueComplete=None, subscribed=None):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}", params={"key": self._apikey, "token": self._token}, data={"name": name, "desc": desc, "closed": closed, "idMembers": idMembers, "idAttachmentCover": idAttachmentCover, "idList": idList, "idLabels": idLabels, "idBoard": idBoard, "pos": pos, "due": due, "dueComplete": dueComplete, "subscribed": subscribed})
        return self.raise_or_json(resp)

    def update_action_comment_idAction(self, idAction, card_id_or_shortlink, text):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/actions/{idAction}/comments", params={"key": self._apikey, "token": self._token}, data={"text": text})
        return self.raise_or_json(resp)

    def update_checklist_checkItem_name_idChecklist_idCheckItem(self, idChecklist, idCheckItem, card_id_or_shortlink, value):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/checklist/{idChecklist}/checkItem/{idCheckItem}/name", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_checklist_checkItem_po_idChecklist_idCheckItem(self, idChecklist, idCheckItem, card_id_or_shortlink, value):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/checklist/{idChecklist}/checkItem/{idCheckItem}/pos", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_checklist_checkItem_state_idChecklist_idCheckItem(self, idChecklist, idCheckItem, card_id_or_shortlink, value):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/checklist/{idChecklist}/checkItem/{idCheckItem}/state", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_checklist_checkItem_idChecklistCurrent_idCheckItem(self, idChecklistCurrent, idCheckItem, card_id_or_shortlink, name=None, state=None, idChecklist=None, pos=None):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/checklist/{idChecklistCurrent}/checkItem/{idCheckItem}", params={"key": self._apikey, "token": self._token}, data={"name": name, "state": state, "idChecklist": idChecklist, "pos": pos})
        return self.raise_or_json(resp)

    def update_checkItem_idCheckItem(self, idCheckItem, card_id_or_shortlink, name=None, state=None, idChecklist=None, pos=None, due=None):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/checkItem/{idCheckItem}", params={"key": self._apikey, "token": self._token}, data={"name": name, "state": state, "idChecklist": idChecklist, "pos": pos, "due": due})
        return self.raise_or_json(resp)

    def update_closed(self, card_id_or_shortlink, value):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/closed", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_desc(self, card_id_or_shortlink, value):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/desc", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_due(self, card_id_or_shortlink, value):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/due", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_dueComplete(self, card_id_or_shortlink, value):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/dueComplete", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_idAttachmentCover(self, card_id_or_shortlink, value):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/idAttachmentCover", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_idBoard(self, card_id_or_shortlink, value, idList=None):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/idBoard", params={"key": self._apikey, "token": self._token}, data={"value": value, "idList": idList})
        return self.raise_or_json(resp)

    def update_idList(self, card_id_or_shortlink, value):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/idList", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_idMember(self, card_id_or_shortlink, value):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/idMembers", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_name(self, card_id_or_shortlink, value):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/name", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_po(self, card_id_or_shortlink, value):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/pos", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def update_sticker_idSticker(self, idSticker, card_id_or_shortlink, top=None, left=None, zIndex=None, rotate=None):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/stickers/{idSticker}", params={"key": self._apikey, "token": self._token}, data={"top": top, "left": left, "zIndex": zIndex, "rotate": rotate})
        return self.raise_or_json(resp)

    def update_subscribed(self, card_id_or_shortlink, value):
        resp = requests.put(f"https://trello.com/1/cards/{card_id_or_shortlink}/subscribed", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def new(self, name, idList, desc=None, pos=None, due=None, dueComplete=None, idMembers=None, idLabels=None, urlSource=None, fileSource=None, idCardSource=None, keepFromSource=None):
        resp = requests.post("https://trello.com/1/cards", params={"key": self._apikey, "token": self._token}, data={"name": name, "idList": idList, "desc": desc, "pos": pos, "due": due, "dueComplete": dueComplete, "idMembers": idMembers, "idLabels": idLabels, "urlSource": urlSource, "fileSource": fileSource, "idCardSource": idCardSource, "keepFromSource": keepFromSource})
        return self.raise_or_json(resp)

    def new_action_comment(self, card_id_or_shortlink, text):
        resp = requests.post(f"https://trello.com/1/cards/{card_id_or_shortlink}/actions/comments", params={"key": self._apikey, "token": self._token}, data={"text": text})
        return self.raise_or_json(resp)

    def new_attachment(self, card_id_or_shortlink, file=None, url=None, name=None, mimeType=None):
        resp = requests.post(f"https://trello.com/1/cards/{card_id_or_shortlink}/attachments", params={"key": self._apikey, "token": self._token}, data={"file": file, "url": url, "name": name, "mimeType": mimeType})
        return self.raise_or_json(resp)

    def new_checklist_checkItem_idChecklist(self, idChecklist, card_id_or_shortlink, name, pos=None, due=None):
        resp = requests.post(f"https://trello.com/1/cards/{card_id_or_shortlink}/checklist/{idChecklist}/checkItem", params={"key": self._apikey, "token": self._token}, data={"name": name, "pos": pos, "due": due})
        return self.raise_or_json(resp)

    def new_checklist_checkItem_convertToCard_idChecklist_idCheckItem(self, idChecklist, idCheckItem, card_id_or_shortlink):
        resp = requests.post(f"https://trello.com/1/cards/{card_id_or_shortlink}/checklist/{idChecklist}/checkItem/{idCheckItem}/convertToCard", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def new_checklist(self, card_id_or_shortlink, value=None, name=None, idChecklistSource=None):
        resp = requests.post(f"https://trello.com/1/cards/{card_id_or_shortlink}/checklists", params={"key": self._apikey, "token": self._token}, data={"value": value, "name": name, "idChecklistSource": idChecklistSource})
        return self.raise_or_json(resp)

    def new_idLabel(self, card_id_or_shortlink, value):
        resp = requests.post(f"https://trello.com/1/cards/{card_id_or_shortlink}/idLabels", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def new_idMember(self, card_id_or_shortlink, value):
        resp = requests.post(f"https://trello.com/1/cards/{card_id_or_shortlink}/idMembers", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def new_label(self, card_id_or_shortlink, color, name=None):
        resp = requests.post(f"https://trello.com/1/cards/{card_id_or_shortlink}/labels", params={"key": self._apikey, "token": self._token}, data={"color": color, "name": name})
        return self.raise_or_json(resp)

    def new_markAssociatedNotificationsRead(self, card_id_or_shortlink):
        resp = requests.post(f"https://trello.com/1/cards/{card_id_or_shortlink}/markAssociatedNotificationsRead", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def new_membersVoted(self, card_id_or_shortlink, value):
        resp = requests.post(f"https://trello.com/1/cards/{card_id_or_shortlink}/membersVoted", params={"key": self._apikey, "token": self._token}, data={"value": value})
        return self.raise_or_json(resp)

    def new_sticker(self, card_id_or_shortlink, image, top, left, zIndex, rotate=None):
        resp = requests.post(f"https://trello.com/1/cards/{card_id_or_shortlink}/stickers", params={"key": self._apikey, "token": self._token}, data={"image": image, "top": top, "left": left, "zIndex": zIndex, "rotate": rotate})
        return self.raise_or_json(resp)

    def delete(self, card_id_or_shortlink):
        resp = requests.delete(f"https://trello.com/1/cards/{card_id_or_shortlink}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def delete_action_comment_idAction(self, idAction, card_id_or_shortlink):
        resp = requests.delete(f"https://trello.com/1/cards/{card_id_or_shortlink}/actions/{idAction}/comments", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def delete_attachment_idAttachment(self, idAttachment, card_id_or_shortlink):
        resp = requests.delete(f"https://trello.com/1/cards/{card_id_or_shortlink}/attachments/{idAttachment}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def delete_checklist_checkItem_idChecklist_idCheckItem(self, idChecklist, idCheckItem, card_id_or_shortlink):
        resp = requests.delete(f"https://trello.com/1/cards/{card_id_or_shortlink}/checklist/{idChecklist}/checkItem/{idCheckItem}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def delete_checkItem_idCheckItem(self, idCheckItem, card_id_or_shortlink):
        resp = requests.delete(f"https://trello.com/1/cards/{card_id_or_shortlink}/checkItem/{idCheckItem}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def delete_checklist_idChecklist(self, idChecklist, card_id_or_shortlink):
        resp = requests.delete(f"https://trello.com/1/cards/{card_id_or_shortlink}/checklists/{idChecklist}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def delete_idLabel_idLabel(self, idLabel, card_id_or_shortlink):
        resp = requests.delete(f"https://trello.com/1/cards/{card_id_or_shortlink}/idLabels/{idLabel}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def delete_idMember_idMember(self, idMember, card_id_or_shortlink):
        resp = requests.delete(f"https://trello.com/1/cards/{card_id_or_shortlink}/idMembers/{idMember}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def delete_membersVoted_idMember(self, idMember, card_id_or_shortlink):
        resp = requests.delete(f"https://trello.com/1/cards/{card_id_or_shortlink}/membersVoted/{idMember}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)

    def delete_sticker_idSticker(self, idSticker, card_id_or_shortlink):
        resp = requests.delete(f"https://trello.com/1/cards/{card_id_or_shortlink}/stickers/{idSticker}", params={"key": self._apikey, "token": self._token}, data=None)
        return self.raise_or_json(resp)


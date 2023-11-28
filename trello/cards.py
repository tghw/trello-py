# TODO: write up gets
"""
get Members
get pluginData
get Stickers
"""


from .api_client import APIClient

REFERENCE_TARGET = 'cards'


class Cards:
    __module__ = 'trello'

    def __init__(self, apikey, token):
        self._api_client = APIClient(apikey, token)

    ### GET SECTION ###

    def get_card(self, card_id):
        return self._api_client.get(REFERENCE_TARGET, card_id)

    def get_card_field(self, card_id: str, field: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, card_id, child=field, **kwargs)

    def get_card_actions(self, card_id: str, filter: str = 'all', limit: int = 1000, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, card_id, child='actions', filter=filter, limit=limit, **kwargs)

    def get_card_attachments(self, card_id: str, fields: str = 'all', filter: str = 'false', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, card_id, child='attachments', filter=filter, fields=fields, **kwargs)

    def get_card_specific_attachment(self, card_id: str, attachment_id: str, fields: str = None, **kwargs):
        if fields:
            kwargs['fields'] = fields
        return self._api_client.get(REFERENCE_TARGET, card_id, child='attachments', child_id=attachment_id, **kwargs)

    def get_board(self, card_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, card_id, child_id='board', fields=fields, **kwargs)

    def get_card_checkItems(self, card_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, card_id, 'checkItemStates', fields=fields, **kwargs)

    def get_card_checkLists(self, card_id: str, checkItems: str = 'all', checkItem_fields: str = None, filter: str= 'all', fields: str = None, **kwargs):
        if checkItems:
            kwargs['checkItems'] = checkItems
        if checkItem_fields:
            kwargs['checkItem_fields'] = checkItem_fields
        if filter:
            kwargs['filter'] = filter
        if fields:
            kwargs['fields'] = fields
        return self._api_client.get(REFERENCE_TARGET, card_id, child='checklists', **kwargs)

    def get_card_checkItem(self, card_id: str, idcheckItem, fields: str = None, **kwargs):
        if fields:
            kwargs['fields'] = fields
        return self._api_client.get(REFERENCE_TARGET, card_id, child='checkItem', child_id=idcheckItem, **kwargs)

    def get_card_list(self, card_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, card_id, child='list', fields=fields, **kwargs)

    def get_card_customFields(self, card_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, card_id, child='customFieldItems', **kwargs)

    ### POST SECTION ###

    def new_card(self, idList: str = None, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, require_target_id=False, idList=idList, **kwargs)

    def new_comment(self, card_id: str, text: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, card_id, child='actions/comments', text=text, **kwargs)

    def add_card_label(self, card_id: str, label_id: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, card_id, child='idLabels', value=label_id, **kwargs)

    def add_card_member(self, card_id: str, member_id: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, card_id, child='idMembers', value=member_id, **kwargs)

    def create_label(self, card_id: str, color: str, name: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, card_id, child='labels', color=color, name=name, **kwargs)

    def mark_as_read(self, card_id, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, card_id, child='markAssociatedNotificationsRead', **kwargs)

    ### PUT SECTION ###

    def update_card(self, card_id: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, target_id=card_id, **kwargs)

    def update_card_cover_color(self, card_id: str, color: str, size: str = 'normal', brightness: str = 'light'):
        return self._api_client.put(REFERENCE_TARGET, card_id, cover={'color': color, 'size': size, 'brightness': brightness})

    def update_card_checkItem(self, card_id: str, idCheckItem: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, card_id, child='checkItem', child_id=idCheckItem, **kwargs)

    def update_card_comment(self, card_id: str, idAction: str, text: str, **kwargs):
        address_addition = f"{idAction}/comments"
        return self._api_client.put(REFERENCE_TARGET, card_id, child='actions', child_id=address_addition, text=text, **kwargs)

    def update_card_customField(self, card_id: str, idCustomField: str, **kwargs):
        address_addition = f"{idCustomField}/item"
        return self._api_client.put(REFERENCE_TARGET, card_id, child='customField', child_id=address_addition, **kwargs)

    def update_card_multiple_customField(self, card_id: str, customFieldItems, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, card_id, child='customFields', customFieldItems=customFieldItems, **kwargs)

    def update_checkItem_on_checkList(self, card_id: str, idCheckItem: str, idChecklist: str, pos: str|int = None, **kwargs):
        address_addition = f"checklist/{idChecklist}/checkItem/{idCheckItem}"
        if pos:
            kwargs['pos'] = pos
        return self._api_client.put(REFERENCE_TARGET, card_id, child=address_addition, **kwargs)

    ### Delete Section ###

    def delete_card(self, card_id: str):
        return self._api_client.delete(REFERENCE_TARGET, card_id)

    def delete_card_attachment(self, card_id: str, idAttachment: str):
        return self._api_client.delete(REFERENCE_TARGET, card_id, child='attachments', child_id=idAttachment)

    def delete_card_checkItem(self, card_id: str, idCheckItem: str):
        return self._api_client.delete(REFERENCE_TARGET, card_id, child='checkItem', child_id=idCheckItem)

    def delete_card_comment(self, card_id: str, idAction: str):
        return self._api_client.delete(REFERENCE_TARGET, card_id, child='actions', child_id=idAction)

    def delete_card_label(self, card_id: str, idLabel: str):
        return self._api_client.delete(REFERENCE_TARGET, card_id, child='idLabels', child_id=idLabel)

    def delete_card_member(self, card_id: str, idMember: str):
        return self._api_client.delete(REFERENCE_TARGET, card_id, child='idMembers', child_id=idMember)

    def delete_card_checkList(self, card_id: str, idChecklist: str):
        return self._api_client.delete(REFERENCE_TARGET, card_id, child='checklists', child_id=idChecklist)


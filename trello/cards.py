# TODO: write up gets
"""
get Members
get pluginData
get Stickers
"""


from api_client import APIClient

REFERENCE_TARGET = 'cards'


class Cards:

    def __init__(self, apikey, token):
        self._api_client = APIClient(apikey, token)

    ### GET SECTION ###

    def get_card(self, card_id):
        return self._api_client.get(REFERENCE_TARGET, card_id)

    def get_field(self, card_id: str, field: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, card_id, child=field, **kwargs)

    def get_actions(self, card_id: str, filter: str = 'all', limit: int = 1000, **kwargs):
        if filter:
            kwargs['filter'] = filter
        kwargs['limit'] = limit
        return self._api_client.get(REFERENCE_TARGET, card_id, child='actions', **kwargs)

    def get_attachments(self, card_id: str, fields: str = None, filter: str = None, **kwargs):
        if fields:
            kwargs['filter'] = fields
        if filter:
            kwargs['filter'] = filter
        return self._api_client.get(REFERENCE_TARGET, card_id, child='attachments', **kwargs)

    def get_specific_attachment(self, card_id: str, attachment_id: str, fields: str = None, **kwargs):
        if fields:
            kwargs['fields'] = fields
        return self._api_client.get(REFERENCE_TARGET, card_id, child='attachments', child_id=attachment_id, **kwargs)

    def get_board(self, card_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, card_id, child_id='board', **kwargs)

    def get_checkItems(self, card_id: str, fields: str = 'all', **kwargs):
        if fields:
            kwargs['fields'] = fields
        return self._api_client.get(REFERENCE_TARGET, card_id, 'checkItemStates', **kwargs)

    def get_checkLists(self, card_id: str, checkItems: str = 'all', checkItem_fields: str = None, filter: str= 'all', fields: str = None, **kwargs):
        if checkItems:
            kwargs['checkItems'] = checkItems
        if checkItem_fields:
            kwargs['checkItem_fields'] = checkItem_fields
        if filter:
            kwargs['filter'] = filter
        if fields:
            kwargs['fields'] = fields
        return self._api_client.get(REFERENCE_TARGET, card_id, child='checklists', **kwargs)

    def get_checkItem(self, card_id: str, idcheckItem, fields: str = None, **kwargs):
        if fields:
            kwargs['fields'] = fields
        return self._api_client.get(REFERENCE_TARGET, card_id, child='checkItem', child_id=idcheckItem, **kwargs)

    def get_list(self, card_id: str, fields: str = 'all', **kwargs):
        if fields:
            kwargs['field'] = fields
        return self._api_client.get(REFERENCE_TARGET, card_id, child='list', **kwargs)

    def get_customFields(self, card_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, card_id, child='customFieldItems', **kwargs)

    ### POST SECTION ###

    def new_card(self, idList: str = None, query: dict = None):
        query['idList'] = idList
        return self._api_client.post(REFERENCE_TARGET, require_target_id=False, query=query)

    def new_comment(self, card_id: str, text: str):
        return self._api_client.post(REFERENCE_TARGET, card_id, child='actions/comments', query={'text': text})

    def add_label(self, card_id: str, label_id: str):
        return self._api_client.post(REFERENCE_TARGET, card_id, child='idLabels', query={'value': label_id})

    def add_member(self, card_id: str, member_id: str):
        return self._api_client.post(REFERENCE_TARGET, card_id, child='idMembers', query={'value': member_id})

    def create_label(self, card_id: str, color: str, name: str):
        return self._api_client.post(REFERENCE_TARGET, card_id, child='labels', query={'color': color, 'name': name})

    def mark_as_read(self, card_id):
        return self._api_client.post(REFERENCE_TARGET, card_id, child='markAssociatedNotificationsRead')

    ### PUT SECTION ###

    def update_card(self, card_id: str, query: dict = None):
        return self._api_client.put(REFERENCE_TARGET, target_id=card_id, query=query)

    def update_cover_color(self, card_id: str, color: str, size: str = 'normal', brightness: str = 'light'):
        return self._api_client.put(REFERENCE_TARGET, card_id, query={"cover": { 'color': color, 'size': size, 'brightness': brightness}})

    def update_checkItem(self, card_id: str, idCheckItem: str, query: dict):
        return self._api_client.put(REFERENCE_TARGET, card_id, child='checkItem', child_id=idCheckItem, query=query)

    def update_comment(self, card_id: str, idAction: str, text: str):
        address_addition = f"{idAction}/comments"
        return self._api_client.put(REFERENCE_TARGET, card_id, child='actions', child_id=address_addition, query={'text': text})

    def update_card_customField(self, card_id: str, idCustomField: str, query: dict):
        address_addition = f"{idCustomField}/item"
        return self._api_client.put(REFERENCE_TARGET, card_id, child='customField', child_id=address_addition, query={'value': query})

    def update_card_multiple_customField(self, card_id: str, query_list):
        return self._api_client.put(REFERENCE_TARGET, card_id, child='customFields', query={'customFieldItems': query_list})

    def update_checkItem_on_checkList(self, card_id: str, idCheckItem: str, idChecklist: str, query: dict = None, pos: str|int = None):
        address_addition = f"checklist/{idChecklist}/checkItem/{idCheckItem}"
        if query is None:
            query = dict()
        if pos:
            query['pos'] = pos
        return self._api_client.put(REFERENCE_TARGET, card_id, child=address_addition, query=query)

    ### Delete Section ###

    def delete_card(self, card_id: str):
        return self._api_client.delete(REFERENCE_TARGET, card_id)

    def delete_attachment(self, card_id: str, idAttachment: str):
        return self._api_client.delete(REFERENCE_TARGET, card_id, child='attachments', child_id=idAttachment)

    def delete_checkItem(self, card_id: str, idCheckItem: str):
        return self._api_client.delete(REFERENCE_TARGET, card_id, child='checkItem', child_id=idCheckItem)

    def delete_comment(self, card_id: str, idAction: str):
        return self._api_client.delete(REFERENCE_TARGET, card_id, child='actions', child_id=idAction)

    def delete_card_label(self, card_id: str, idLabel: str):
        return self._api_client.delete(REFERENCE_TARGET, card_id, child='idLabels', child_id=idLabel)

    def delete_member(self, card_id: str, idMember: str):
        return self._api_client.delete(REFERENCE_TARGET, card_id, child='idMembers', child_id=idMember)

    def delete_card_checkList(self, card_id: str, idChecklist: str):
        return self._api_client.delete(REFERENCE_TARGET, card_id, child='checklists', child_id=idChecklist)


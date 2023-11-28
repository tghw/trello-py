from .api_client import APIClient

REFERENCE_TARGET = 'lists'


class List:
    __module__ = 'trello'

    def __init__(self, apikey, token):
        self._api_client = APIClient(apikey, token)

    ### GET Section ###

    def get_checklist(self, list_id: str, fields: str = None, **kwargs):
        if fields: kwargs['fields'] = fields
        return self._api_client.get(REFERENCE_TARGET, list_id, **kwargs)

    def get_checklist_actions(self, list_id: str, filter: str = None, **kwargs):
        if filter: kwargs['filter'] = filter
        return self._api_client.get(REFERENCE_TARGET, list_id, **kwargs)

    def get_board(self, list_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, list_id, fields=fields, **kwargs)

    def get_cards(self, list_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, list_id, child='cards', **kwargs)

    ### POST Section ###

    def new_list(self, name: str, idBoard: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, require_target_id = False, name=name, idBoard=idBoard, **kwargs)

    def archive_cards(self, list_id: str):
        return self._api_client.post(REFERENCE_TARGET, list_id, child='archiveAllCards')

    def move_all_cards(self, list_id: str, to_idBoard: str, to_idList: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, list_id, child='moveAllCards', idBoard=to_idBoard, idList=to_idList, **kwargs)

    ### PUT Section ###
    def update_checklist(self, list_id: str, name: str = None, to_idBoard: str = None, **kwargs):
        if name: kwargs['name'] = name
        if name: kwargs['idBoard'] = to_idBoard
        return self._api_client.put(REFERENCE_TARGET, list_id, **kwargs)

    def archive_or_unarchive_checklist(self, list_id: str, archive: bool = False, unarchive: bool = False, **kwargs):
        if archive: kwargs['value'] = 'true'
        if unarchive: kwargs['value'] = 'false'
        return self._api_client.put(REFERENCE_TARGET, list_id, child='closed', **kwargs)

    def move_checklist_to_board(self, list_id: str, to_idBoard: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, list_id, child='idBoard', value=to_idBoard, **kwargs)

    def update_checklist_field(self, list_id: str, field: str, field_value: str|int, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, list_id, child=field, value=field_value, **kwargs)

    ### Delete/Archive Section ###

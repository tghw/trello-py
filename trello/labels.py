from .api_client import APIClient

REFERENCE_TARGET = 'labels'


class Labels:

    def __init__(self, apikey, token):
        self._api_client = APIClient(apikey, token)

    ### Get Section ###

    def get_label(self, label_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, label_id, fields=fields, **kwargs)

    ### Post Section ###

    def add_label(self, name: str, color: str, board_id: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, required_target_id=False, name=name, color=color, idBoard=board_id, **kwargs)

    ### Put Section ###

    def update_label(self, label_id: str, name: str = None, color: str = None, **kwargs):
        if name: kwargs['name'] = name
        if color: kwargs['color'] = color
        return self._api_client.put(REFERENCE_TARGET, label_id, **kwargs)

    def update_label_field(self, label_id: str, field: str, value: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, label_id, child=field, value=value, **kwargs)

    ### Delete Section ###

    def delete_label(self, label_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, label_id, **kwargs)

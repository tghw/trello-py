from .api_client import APIClient

REFERENCE_TARGET = "customFields"

class Customfields:

    def __init__(self, apikey, token):
        self._api_client = APIClient(apikey, token)

    ### Get Section ###

    def get_customField(self, customfields_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, customfields_id, **kwargs)

    def get_field_options(self, customfields_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, customfields_id, child='options', **kwargs)

    def get_specfics(self, customfields_id: str, customfieldoption_id: str, **kwargs ):
        return self._api_client.get(REFERENCE_TARGET, customfields_id, child='options', child_id=customfieldoption_id, **kwargs)

    ### Post Section ###

    def new_board_field(self, model_id: str, name: str, field_type: str, pos: str | int, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, require_target_id=False, idModel=model_id, modelType='board', name=name, type=field_type, pos=pos, **kwargs)

    def new_option(self, customfields_id: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, customfields_id, child='options', **kwargs)

    ### Put Section ###

    def update_definition(self, customfields_id: str, name: str = None, pos: str | int = None, **kwargs):
        if name: kwargs['name'] = name
        if pos: kwargs['pos'] = pos
        return self._api_client.put(REFERENCE_TARGET, customfields_id, **kwargs)

    ### Delete Section ###

    def delete_field(self, customfields_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, customfields_id, **kwargs)

    def delete_option(self, customfields_id: str, field_option_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, customfields_id, child='options', child_id=field_option_id)


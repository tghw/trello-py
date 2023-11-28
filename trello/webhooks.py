from .api_client import APIClient

REFERENCE_TARGET = 'webhooks'


class Webhooks:
    __module__ = 'trello'

    def __init__(self, apikey, token):
        self._api_client = APIClient(apikey, token)

    ### Get Section ###

    def get_webhooks(self, webhook_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, webhook_id, **kwargs)

    def get_webhook_field(self, webhook_id: str, field: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, webhook_id, child=field, **kwargs)

    ### Post Section ###

    def new_webhook(self, model_id: str, callbackURL: str = 'url', **kwargs):
        return self._api_client.post(REFERENCE_TARGET, require_target_id=False, idModel=model_id, callbackURL=callbackURL, **kwargs)

    ### Put Section ###

    def update_webhook(self, webhook_id: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, webhook_id, **kwargs)

    ### Delete Section ###

    def delete_webhook(self, webhook_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, webhook_id, **kwargs)

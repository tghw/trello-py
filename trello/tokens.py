from .api_client import APIClient

REFERENCE_TARGET = 'tokens'


class Tokens:
    __module__ = 'trello'

    def __init__(self, apikey, token):
        self._api_client = APIClient(apikey, token)

    ### Get Section ###

    def get_token_info(self, token: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, token, fields=fields, **kwargs)

    def get_token_member(self, token: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, token, child='member', fields=fields, **kwargs)

    def get_token_webhooks(self, token: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, token, child='webhooks', **kwargs)

    def get_token_webhook_specifics(self, token: str, webhook_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, token, child='webhooks', child_id=webhook_id, **kwargs)

    ### Post Section ###

    def create_token_webhook(self, token: str, idModel: str, callbackURL: str = 'url', **kwargs):
        return self._api_client.post(REFERENCE_TARGET, token, child='webhooks', callbackURL=callbackURL, idModel=idModel, **kwargs)

    ### Put Section ###

    def update_token_webhook(self, token: str, webhook_id: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, token, child='webhooks', child_id=webhook_id, **kwargs)

    ### Delete Section ###

    def delete_token_webhook(self, token: str, webhook_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, token, child='webhooks', child_id=webhook_id, **kwargs)

    def delete_token(self, token: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, token, **kwargs)



from .api_client import APIClient

REFERENCE_TARGET = 'labels'


class Actions:

    def __init__(self, apikey, token):
        self._api_client = APIClient(apikey, token)

    ### Get Section ###

    def get_action(self, action_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, action_id, **kwargs)

    def get_action_field(self, action_id: str, field: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, action_id, child=field, **kwargs)

    def get_action_board(self, action_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, action_id, child='board', fields=fields, **kwargs)

    def get_action_card(self, action_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, action_id, child='card', fields=fields, **kwargs)

    def get_action_member(self, action_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, action_id, child='member', fields=fields, **kwargs)

    def get_action_member_creator(self, actions_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, actions_id, child='memberCreator', fields=fields, **kwargs)

    def get_action_organization(self, actions_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, actions_id, child='organization', fields=fields, **kwargs)

    def get_action_reactions(self, action_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, action_id, child='reactions', **kwargs)

    def get_action_reaction_info(self, action_id: str, reaction_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, action_id, child='reactions', child_id=reaction_id, **kwargs)

    def get_action_summary(self, action_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, action_id, child='reactionsSummary', **kwargs)

    ### Post Section ###

    def new_reaction(self, action_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, action_id, child='reactions', **kwargs)

    ### Put Section ###

    def update_action(self, action_id: str, text: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, action_id, text=text, **kwargs)

    def update_comment(self, action_id: str, value: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, action_id, child='text', value=value, **kwargs)

    ### Delete Section ###

    def delete_action(self, action_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, action_id, **kwargs)

    def delete_reaction(self, action_id: str, reaction_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, action_id, child='reactions', child_id=reaction_id, **kwargs)
    
from .api_client import APIClient

REFERENCE_TARGET = 'notifications'


class Notification:

    def __init__(self, apikey, token):
        self._api_client = APIClient(apikey, token)

    ### Get Section ###

    def get_notification(self, notification_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, notification_id, **kwargs)

    def get_notification_field(self, notification_id: str, field: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, notification_id, child=field, **kwargs)

    def get_board_notification(self, notification_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, notification_id, child='board', fields=fields, **kwargs)

    def get_card_notification(self, notification_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, notification_id, child='card', fields=fields, **kwargs)

    def get_list_notification(self, notification_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, notification_id, child='list', fields=fields, **kwargs)

    def get_member_notification_noncreator(self, notification_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, notification_id, child='member', fields=fields, **kwargs)

    def get_member_notification_creator(self, notification_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, notification_id, child='memberCreator', fields=fields, **kwargs)

    def get_organization_notification(self, notification_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, notification_id, child='organization', fields=fields, **kwargs)

    ### Post Section ###

    def mark_all_notifications_read(self, ids: str, read: bool | str = 'true', **kwargs):
        if read: kwargs['read'] = 'true'
        else: kwargs['read'] = 'false'
        return self._api_client.post(REFERENCE_TARGET, 'all/read', ids=ids, **kwargs)

    ### Put Section ###

    def update_notifications(self, notification_id: str, value: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, notification_id, child='unread', value=value, **kwargs)

    ### Delete Section ###

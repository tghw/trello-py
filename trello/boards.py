from .api_client import APIClient

REFERENCE_TARGET = 'boards'


class Boards:

    def __init__(self, apikey, token):
        self._api_client = APIClient(apikey, token)

    ### Get Section ###

    def get_board(self, board_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, board_id, **kwargs)

    def get_board_field(self, board_id: str, field: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, board_id, child=field, **kwargs)

    def get_board_actions(self, board_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, board_id, child='actions', **kwargs)

    def get_card(self, board_id: str, card_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, board_id, child='cards', child_id=card_id, **kwargs)

    def get_board_stars(self, board_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, board_id, child='boardStars', **kwargs)

    def get_board_checklists(self, board_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, board_id, child='checklists', **kwargs)

    def get_all_cards(self, board_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, board_id, child='cards', **kwargs)

    def get_filtered_cards(self, board_id: str, filter: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, board_id, child='cards', child_id=filter, **kwargs)

    def get_board_customfields(self, board_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, board_id, child='customFields', **kwargs)

    def get_board_label(self, board_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, board_id, child='labels', **kwargs)

    def get_board_lists(self, board_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, board_id, child='lists', **kwargs)

    def get_filtered_lists(self, board_id: str, filter: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, board_id, child='lists', child_id=filter, **kwargs)

    def get_board_members(self, board_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, board_id, child='members', **kwargs)

    def get_enabled_power_ups(self, board_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, board_id, child='boardPlugins', **kwargs)

    def get_power_up_filtered(self, board_id: str, filter: str = 'enabled', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, board_id, child='plugins', filter=filter, **kwargs)

    ### Post Section ###

    def add_board_label(self, board_id: str, name: str, color: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, board_id, child='labels', name=name, color=color, **kwargs)

    def add_board_list(self, board_id: str, name: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, board_id, child='lists', name=name, **kwargs)

    def new_board(self, name: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, require_target_id=False, name=name, **kwargs)

    def add_board_calendarKey(self, board_id: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, board_id, child='calendarKey/generate', **kwargs)

    def add_board_emailKey(self, board_id: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, board_id, child='emailKey/generate', **kwargs)

    def add_board_tag(self, board_id: str, value: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, board_id, child='idTags', value=value, **kwargs)

    def mark_viewed(self, board_id: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, board_id, child='markedAsViewed', **kwargs)

    def enable_powerup(self, board_id: str, plugin_id: str = None, **kwargs):
        if plugin_id: kwargs['idPlugin'] = plugin_id
        return self._api_client.post(REFERENCE_TARGET, board_id, child='boardPlugins', **kwargs)

    ### Put Section ###

    def update_board(self, board_id: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, board_id, **kwargs)

    def invite_members_by_email(self, board_id: str, email: str, fullName: str, type_value: str = 'normal', **kwargs):
        return self._api_client.put(REFERENCE_TARGET, board_id, child='members', email=email, type=type_value, fullName=fullName, **kwargs)

    def add_member(self, board_id: str, member_id: str, type_value: str = 'normal', allowBillableGuest: str = 'false', **kwargs):
        return self._api_client.put(REFERENCE_TARGET, board_id, child='members', child_id=member_id, type=type_value, allowBillableGuest=allowBillableGuest, **kwargs)

    def update_member_membership(self, board_id: str, membership_id: str, type_value: str = 'normal', **kwargs):
        return self._api_client.put(REFERENCE_TARGET, board_id, child='memberships', child_id=membership_id, type=type_value, **kwargs)

    def update_emailPosition_pref(self, board_id: str, value: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, board_id, child='myPrefs/emailPosition', value=value, **kwargs)

    def update_emailList_pref(self, board_id: str, value: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, board_id, child='myPrefs/idEmailList', value=value, **kwargs)

    def update_showListGuide_pref(self, board_id: str, value: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, board_id, child='myPrefs/showListGuide', value=value, **kwargs)

    def update_showSidebar_pref(self, board_id: str, value: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, board_id, child='myPrefs/showSidebar', value=value, **kwargs)

    def update_showSidebarActivity_pref(self, board_id: str, value: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, board_id, child='myPrefs/showSidebarActivity', value=value, **kwargs)

    def update_showSidebarBoardActions_pref(self, board_id: str, value: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, board_id, child='myPrefs/showSidebarBoardActions', value=value, **kwargs)

    def update_showSidebarMembers_pref(self, board_id: str, value: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, board_id, child='myPrefs/showSidebarMembers', value=value, **kwargs)

    ### Delete Section ###

    def delete_board(self, board_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, board_id, **kwargs)

    def remove_member(self, board_id: str, member_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, board_id, child='members', child_id=member_id, **kwargs)

    def disable_powerup(self, board_id: str, plugin_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, board_id, child='boardPlugins', child_id=plugin_id, **kwargs)




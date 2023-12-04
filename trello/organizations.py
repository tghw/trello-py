from .api_client import APIClient

REFERENCE_TARGET = 'organizations'


class Organizations:

    def __init__(self, apikey, token):
        self._api_client = APIClient(apikey, token)

    ### Get Section ###

    def get_organization(self, organization_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, organization_id, **kwargs)

    def get_organization_field(self, organization_id: str, field: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, organization_id, child=field, **kwargs)

    def get_organization_actions(self, organization_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, organization_id, child='actions', **kwargs)

    def get_organization_boards(self, organization_id: str, filter: str = 'all', fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, organization_id, child='boards', filter=filter, fields=fields, **kwargs)

    def get_organization_exports(self, organization_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, organization_id, child='exports', **kwargs)
    
    def get_organization_members(self, organization_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, organization_id, child='members', **kwargs)

    def get_organization_memberships(self, organization_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, organization_id, child='memberships', **kwargs)

    def get_organization_membership(self, organization_id: str, membership_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, organization_id, child='memberships', child_id=membership_id, **kwargs)

    def get_organization_pluginData_scope(self, organization_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, organization_id, child='pluginData', **kwargs)

    def get_organization_tags(self, organization_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, organization_id, child='tags', **kwargs)

    def get_organization_new_billable_guest(self, organizaiton_id: str, board_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, organizaiton_id, child='newBillableGuests', child_id=board_id, **kwargs)

    ### Post Section ###

    def new_workspace(self, displayName: str, desc: str, name: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, required_target_id=False, displayName=displayName, desc=desc, name=name, **kwargs)

    def create_exports(self, workspace_id: str, attachments: bool | str, **kwargs):
        if attachments: kwargs['attachments'] = 'true'
        else: kwargs['attachments'] = 'false'
        return self ._api_client.post(REFERENCE_TARGET, workspace_id, child='exports', **kwargs)

    def create_tag(self, organization_id: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, organization_id, child='tags', **kwargs)

    def update_workspace_logo(self, organization_id: str, file, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, organization_id, child='logo', file=file, **kwargs)

    ### Put Section ###

    def update_organization(self, organization_id: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, organization_id, **kwargs)

    def update_organization_members(self, organization_id: str, email: str, fullName: str, type_value: str = 'normal', **kwargs):
        return self._api_client.put(REFERENCE_TARGET, organization_id, child='members', email=email, fullName=fullName, type=type_value, **kwargs)

    def update_or_add_workspace_member(self, organization_id: str, member_id: str, type_value: str = 'normal', **kwargs):
        return self._api_client.put(REFERENCE_TARGET, organization_id, child='members', child_id=member_id, type=type_value, **kwargs)

    def deactivate_or_reactivate_workspace_member(self, organization_id: str, member_id: str, value: bool | str = False, **kwargs):
        if value: kwargs['value'] = 'true'
        else: kwargs['value'] = 'false'
        return self._api_client.put(REFERENCE_TARGET, organization_id, child='members', child_id=f'{member_id}/deactivated', **kwargs)

    ### Delete Section ###

    def delete_organization(self, organization_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, organization_id, **kwargs)

    def remove_workspace_member(self, organization_id: str, member_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, organization_id, child='members', child_id=member_id, **kwargs)

    def delete_workspace_logo(self, organization_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, organization_id, child='logo', **kwargs)

    def delete_member_all_workspace(self, organization_id: str, member_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, organization_id, child='members', child_id=f'{member_id}/all', **kwargs)

    def delete_workspace_google_apps(self, organization_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, organization_id, child='prefs/associatedDomain', **kwargs)

    def remove_workspace_email_restriction(self, organization_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, organization_id, child='prefs/orgInviteRestrict', **kwargs)

    def delet_organization_tag(self, organization_id: str, tag_id: str, **kwargs):
        return self._api_client.delete(REFERENCE_TARGET, organization_id, child='tags', child_id=tag_id, **kwargs)


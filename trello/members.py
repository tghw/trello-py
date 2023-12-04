from .api_client import APIClient

REFERENCE_TARGET = 'members'


class Members:

    def __init__(self, apikey, token):
        self._api_client = APIClient(apikey, token)

    ### Get Section ###

    def get_member(self, username_or_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, **kwargs)

    def get_member_field(self, username_or_id: str, field: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child=field, **kwargs)

    def get_member_actions(self, username_or_id: str, filter: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='actions', filter=filter, **kwargs)

    def get_member_custom_background(self, username_or_id: str, filter: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='boardBackgrounds', filter=filter, **kwargs)

    def get_member_background(self, username_or_id: str, background_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='boardBackgrounds', child_id=background_id, fields=fields, **kwargs)

    def get_member_stars(self, username_or_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='boardStars', **kwargs)

    def get_member_specific_boarStar(self, username_or_id: str, star_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='boardStars', child_id=star_id, **kwargs)

    def get_list_member_boards(self, username_or_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='boards', **kwargs)

    def get_member_board_invite(self, username_or_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='boardsInvited', fields=fields, **kwargs)

    def get_member_cards(self, username_or_id: str, filter: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='cards', filter=filter, **kwargs)

    def get_member_customEmojis(self, username_or_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='customEmoji', **kwargs)

    def get_member_specific_emoji(self, username_or_id: str, emoji_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='customEmoji', child_id=emoji_id, **kwargs)

    def get_member_stickers(self, username_or_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='customStickers', **kwargs)

    def get_member_specific_sticker(self, username_or_id: str, sticker_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='customStickers', child_id=sticker_id, fields=fields, **kwargs)

    def get_member_notification(self, username_or_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='notifications', **kwargs)

    def get_member_workspace(self, username_or_id: str, filter: str = 'all', fields: str = 'all', paid_account: bool = False, **kwargs):
        if paid_account: kwargs['paid_account'] = 'true'
        else: kwargs['paid_account'] = 'false'
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='organizations', filter=filter, fields=fields, **kwargs)

    def get_member_workspace_invites(self, username_or_id: str, fields: str = 'all', **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='organizationsInvited', fields=fields, **kwargs)

    def get_members_saved_searches(self, username_or_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='savedSearches', **kwargs)

    def get_member_saved_search(self, username_or_id: str, search_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='savedSearches', child_id=search_id, **kwargs)

    def get_member_token(self, username_or_id: str, **kwargs):
        return self._api_client.get(REFERENCE_TARGET, username_or_id, child='tokens', **kwargs)

    ### Post Section ###

    def new_boardBackground(self, username_or_id: str, file: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, username_or_id, child='boardBackgrounds', file=file, **kwargs)

    def create_star_board(self, username_or_id: str, board_id: str, pos: int | str = 'top', **kwargs):
        return self._api_client.post(REFERENCE_TARGET, username_or_id, child='boardStars', idBoard=board_id, pos=pos,**kwargs)

    def dismiss_member_message(self, username_or_id: str, message_id: str, **kwargs):
        return self._api_client.post(REFERENCE_TARGET, username_or_id, child='oneTimeMessagesDismissed', value=message_id, **kwargs)

    ### Put Section ###

    def update_member(self, username_or_id: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, username_or_id, **kwargs)

    def update_member_board_background(self, username_or_id: str, background_id: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, username_or_id, child='boardBackgrounds', child_id=background_id, **kwargs)

    def update_position_member_boardStar(self, username_or_id: str, star_id: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, username_or_id, child='boardStars', child_id=star_id, **kwargs)

    def update_member_specific_custom_board_background(self, username_or_id: str, background_id: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, username_or_id, child='customBoardBackgrounds', child_id=background_id, **kwargs)

    def update_saved_search(self, username_or_id: str, search_id: str, **kwargs):
        return self._api_client.put(REFERENCE_TARGET, username_or_id, child='savedSearches', child_id=search_id, **kwargs)

    def update_member_specific_channel_block_notification(self, username_or_id: str, blackedKeys: str, channel: str = 'email', **kwargs):
        return self._api_client.put(REFERENCE_TARGET, username_or_id, child='notificationsChannelSettings', blockedKeys=blackedKeys, channel=channel, **kwargs)

    ### Delete Section ###


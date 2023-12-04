from .api_client import APIClient
from .actions import Actions
from .boards import Boards
from .cards import Cards
from .checklists import Checklists
from .customfields import CustomFields
from .labels import Labels
from .lists import List
from .members import Members
from .notifications import Notification
from .organizations import Organizations
from .search import Search
from .tokens import Tokens
from .webhooks import Webhooks


class TrelloAPI:
    def __init__(self, apikey, token=None):
        if not apikey or not isinstance(apikey, str):
            raise ValueError("An API key must be provided and must be a string.")

        if token is not None and not isinstance(token, str):
            raise ValueError("If provided, the token must be a string.")

        self._apikey = apikey
        self._token = token

    def set_token(self, token):
        self._token = token

    def Actions(self):
        return Actions(self._apikey, self._token)

    def Boards(self):
        return Boards(self._apikey, self._token)

    def Cards(self):
        return Cards(self._apikey, self._token)

    def Checklists(self):
        return Checklists(self._apikey, self._token)

    def CustomFields(self):
        return CustomFields(self._apikey, self._token)

    def Labels(self):
        return Labels(self._apikey, self._token)

    def Lists(self):
        return List(self._apikey, self._token)

    def Members(self):
        return Members(self._apikey, self._token)

    def Notifications(self):
        return Notification(self._apikey, self._token)

    def Organizations(self):
        return Organizations(self._apikey, self._token)

    def Search(self):
        return Search(self._apikey, self._token)

    def Tokens(self):
        return Tokens(self._apikey, self._token)

    def Webhooks(self):
        return Webhooks(self._apikey, self._token)

    def get_token_url(self, app_name, expires='30days', write_access=True):
        return f"https://trello.com/1/authorize?key={self._apikey}&name={app_name}&expiration={expires}&response_type=token&scope={'read,write' if write_access else 'read'}"


__all__ = ['TrelloAPI']

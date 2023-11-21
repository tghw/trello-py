from .api_client import APIClient
from .cards import Cards

"""
class TrelloApi(object):
    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token
        self.actions = Actions(apikey, token)
        self.batches = Batches(apikey, token)
        self.boards = Boards(apikey, token)
        self.cards = Cards(apikey, token)
        self.checklists = Checklists(apikey, token)
        self.labels = Labels(apikey, token)
        self.lists = Lists(apikey, token)
        self.members = Members(apikey, token)
        self.notifications = Notifications(apikey, token)
        self.organizations = Organizations(apikey, token)
        self.search = Search(apikey, token)
        self.tokens = Tokens(apikey, token)
        self.types = Types(apikey, token)
        self.webhooks = Webhooks(apikey, token)

    def set_token(self, token):
        self._token = token
        self.actions._token = token
        self.batches._token = token
        self.boards._token = token
        self.cards._token = token
        self.checklists._token = token
        self.labels._token = token
        self.lists._token = token
        self.members._token = token
        self.notifications._token = token
        self.organizations._token = token
        self.search._token = token
        self.tokens._token = token
        self.types._token = token
        self.webhooks._token = token
"""

 #   def get_token_url(self, app_name, expires='30days', write_access=True):
 #       return f"https://trello.com/1/authorize?key={self._apikey}&name={quote(app_name)}&expiration={expires}&response_type=token&scope={'read,write' if write_access else 'read'}"

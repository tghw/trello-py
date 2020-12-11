import unittest
import webbrowser

from trello import TrelloApi

# API Key from dummy account
API_KEY = 'a66228a769040f4a2739ca6593d6baff'

class _Test(unittest.TestCase):
    @property
    def api(self):
        token = None
        try:
            with open('.token', 'r') as fd:
                token = fd.read().strip()
        except FileNotFoundError:
            token = self.token
        return TrelloApi(API_KEY, token)

    @property
    def token(self):
        print('Opening browser to get new token...')
        api = TrelloApi(API_KEY)
        webbrowser.open(api.get_token_url('Testing Python Package', '30days', False))
        token = input('Trello token:\n')
        with open('.token', 'w') as fd:
            fd.write(token)
        return token

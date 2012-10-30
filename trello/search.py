import json
import requests

class Search(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, query, idOrganizations, idBoards=None, idCards=None, modelTypes=None, board_fields=None, boards_limit=None, card_fields=None, cards_limit=None, card_board=None, card_list=None, card_members=None, organization_fields=None, organizations_limit=None, member_fields=None, members_limit=None, action_fields=None, actions_entities=None, actions_limit=None, actions_since=None, partial=None):
        resp = requests.get("https://trello.com/1/search" % (), params=dict(key=self._apikey, token=self._token, query=query, idOrganizations=idOrganizations, idBoards=idBoards, idCards=idCards, modelTypes=modelTypes, board_fields=board_fields, boards_limit=boards_limit, card_fields=card_fields, cards_limit=cards_limit, card_board=card_board, card_list=card_list, card_members=card_members, organization_fields=organization_fields, organizations_limit=organizations_limit, member_fields=member_fields, members_limit=members_limit, action_fields=action_fields, actions_entities=actions_entities, actions_limit=actions_limit, actions_since=actions_since, partial=partial), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)


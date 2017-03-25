import json
import requests

class Search(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, query, idBoards=None, idOrganizations=None, idCards=None, modelTypes=None, board_fields=None, boards_limit=None, card_fields=None, cards_limit=None, cards_page=None, card_board=None, card_list=None, card_members=None, card_stickers=None, card_attachments=None, organization_fields=None, organizations_limit=None, member_fields=None, members_limit=None, partial=None):
        resp = requests.get("https://trello.com/1/search".format(), params={"key": self._apikey, "token": self._token, "query": query, "idBoards": idBoards, "idOrganizations": idOrganizations, "idCards": idCards, "modelTypes": modelTypes, "board_fields": board_fields, "boards_limit": boards_limit, "card_fields": card_fields, "cards_limit": cards_limit, "cards_page": cards_page, "card_board": card_board, "card_list": card_list, "card_members": card_members, "card_stickers": card_stickers, "card_attachments": card_attachments, "organization_fields": organization_fields, "organizations_limit": organizations_limit, "member_fields": member_fields, "members_limit": members_limit, "partial": partial}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)

    def get_member(self, query, limit=None, idBoard=None, idOrganization=None, onlyOrgMembers=None):
        resp = requests.get("https://trello.com/1/search/members".format(), params={"key": self._apikey, "token": self._token, "query": query, "limit": limit, "idBoard": idBoard, "idOrganization": idOrganization, "onlyOrgMembers": onlyOrgMembers}, data=None)
        resp.raise_for_status()
        return json.loads(resp.text)


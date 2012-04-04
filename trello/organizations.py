import json
import requests

class Organizations(object):
    __module__ = 'trello'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, org_id_or_name, actions=None, action_fields=None, action_limit=None, members=None, member_fields=None, boards=None, board_fields=None, fields=None):
        resp = requests.get("https://trello.com/1/organizations/%s" % (org_id_or_name), params=dict(key=self._apikey, token=self._token, actions=actions, action_fields=action_fields, action_limit=action_limit, members=members, member_fields=member_fields, boards=boards, board_fields=board_fields, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_field(self, field, org_id_or_name):
        resp = requests.get("https://trello.com/1/organizations/%s/%s" % (org_id_or_name, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_action(self, org_id_or_name, filter=None, fields=None, limit=None, page=None, idModels=None):
        resp = requests.get("https://trello.com/1/organizations/%s/actions" % (org_id_or_name), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, limit=limit, page=page, idModels=idModels), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board(self, org_id_or_name, filter=None, fields=None, actions=None, action_fields=None, action_limit=None):
        resp = requests.get("https://trello.com/1/organizations/%s/boards" % (org_id_or_name), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, actions=actions, action_fields=action_fields, action_limit=action_limit), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board_filter(self, filter, org_id_or_name):
        resp = requests.get("https://trello.com/1/organizations/%s/boards/%s" % (org_id_or_name, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member(self, org_id_or_name, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/organizations/%s/members" % (org_id_or_name), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member_filter(self, filter, org_id_or_name):
        resp = requests.get("https://trello.com/1/organizations/%s/members/%s" % (org_id_or_name, filter), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def update(self, org_id_or_name, name=None, displayName=None, desc=None, website=None):
        resp = requests.put("https://trello.com/1/organizations/%s" % (org_id_or_name), params=dict(key=self._apikey, token=self._token), data=dict(name=name, displayName=displayName, desc=desc, website=website))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_desc(self, org_id_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/desc" % (org_id_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_displayName(self, org_id_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/displayName" % (org_id_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_name(self, org_id_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/name" % (org_id_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_website(self, org_id_or_name, value):
        resp = requests.put("https://trello.com/1/organizations/%s/website" % (org_id_or_name), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new(self, name, displayName=None, desc=None, website=None):
        resp = requests.post("https://trello.com/1/organizations" % (), params=dict(key=self._apikey, token=self._token), data=dict(name=name, displayName=displayName, desc=desc, website=website))
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete(self, org_id_or_name):
        resp = requests.delete("https://trello.com/1/organizations/%s" % (org_id_or_name), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    

# TODO: insert logging capability in here?

import requests

MAX_TRELLO_LIMIT = 1000  # current max value allowed by Trello


def _parent_check(parent, target_id, require_target_id):
    if parent is None:
        raise ValueError("Parent target not entered. Example: boards, list, cards")
    elif not isinstance(parent, str):
        raise TypeError("parent parameter not in the right form. Must be (str)")

    if require_target_id:
        if target_id is None:
            raise ValueError("id of the parent target not parsed. Check value entered. Refer to Trello REST Document for details")
        elif not isinstance(target_id, str):
            raise TypeError("id of the parent target is not in the right form. Must be (str)")


def _raise_or_data(resp):
    try:
        resp.raise_for_status()
        # Insert logging for here?
        if resp.ok:
            data = resp.json()
            results_count = len(data) if isinstance(data, list) else 1
            print(f"====================| Ok (HTTP 200) Fetched results {results_count} |====================")
            return data
    except requests.HTTPError as e:
        # Insert logging here?
        # return {"error": "HTTP error occurred", "code": e.response.status_code}
        raise e


class APIClient(object):

    def __init__(self, apikey, token):
        self._apikey = apikey
        self._token = token
        self._base_url = "https://trello.com/1"
        self._init_params = {"key": self._apikey, "token": self._token}

    def _construct_url(self, parent, target_id, child=None, child_id=None):
        url = f"{self._base_url}/{parent}"
        if target_id:
            url += f"/{target_id}"
        if child:
            url += f"/{child}"
            if child_id:
                url += f"/{child_id}"
        return url

    def get(self, parent: str = None, target_id: str = None, child: str = None, child_id: str = None, query: dict = None, **kwargs):

        _parent_check(parent, target_id, require_target_id=True)

        url = self._construct_url(parent, target_id, child, child_id)

        params = self._init_params.copy()

        if query:
            params.update(query)

        limit = kwargs.pop('limit', MAX_TRELLO_LIMIT)  # Extract and remove 'limit' from kwargs
        params['limit'] = limit

        # Update params with the remaining items in kwargs
        params.update(kwargs)

        resp = requests.get(url, params=params)

        return _raise_or_data(resp)

    def post(self, parent: str = None, target_id: str = None, require_target_id: bool = True, child: str = None, child_id: str = None, query: dict = None):

        _parent_check(parent, target_id, require_target_id)

        url = self._construct_url(parent, target_id, child, child_id)

        json_query = self._init_params.copy()

        if query:
            json_query.update(query)

        resp = requests.post(url, json=json_query)

        return _raise_or_data(resp)

    def put(self, parent: str = None, target_id: str = None, child: str = None, child_id: str = None, query: dict = None):

        _parent_check(parent, target_id, require_target_id=True)

        url = self._construct_url(parent, target_id, child, child_id)

        json_query = self._init_params.copy()

        if query:
            json_query.update(query)

        resp = requests.put(url, json=json_query)

        return _raise_or_data(resp)

    def delete(self, parent: str = None, target_id: str = None, child: str = None, child_id: str = None, query: dict = None):

        _parent_check(parent, target_id, require_target_id=True)

        url = self._construct_url(parent, target_id, child, child_id)

        json_query = self._init_params.copy()

        if query:
            json_query.update(query)

        resp = requests.delete(url, json=json_query)

        return _raise_or_data(resp)

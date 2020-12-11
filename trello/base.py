class ApiBase(object):
    def raise_or_json(self, resp):
        resp.raise_for_status()
        return resp.json()
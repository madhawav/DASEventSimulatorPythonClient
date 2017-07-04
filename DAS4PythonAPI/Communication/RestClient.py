import json

import requests
class RestClient(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def _sendGetRequest(self, sub_url, params=None):
        headers = {'content-type': 'text/plain'}
        resp = requests.get(self.base_url + sub_url, params=params, headers = headers)
        return resp

    def _sendPostRequest(self, sub_url, data, params = None):
        headers = {'content-type': 'text/plain'}
        resp = requests.post(self.base_url + sub_url, params=params, data=data, headers = headers)
        return resp
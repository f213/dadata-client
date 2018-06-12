# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from dadata.exceptions import DadataPaymentRequired


class DadataBaseClient(object):

    API_URL = ''

    def __init__(self, key):
        self.api_key = key

    def _request_header(self):
        return {
            'Authorization': 'Token %s' % self.api_key,
        }

    def request(self, json):
        try:
            response = requests.post(
                self.API_URL,
                headers=self._request_header(),
                json=json,
            )
        except requests.exceptions.ConnectTimeout:
            return

        return self._prepare_response(response)

    def _prepare_response(self, respose):
        if respose.status_code == 402:
            raise DadataPaymentRequired()

        if respose.status_code == 200:
            return respose.json()


class DadataBasePaidClient(DadataBaseClient):

    def __init__(self, key, secret):
        self.api_key = key
        self.secret_key = secret

    def _request_header(self):
        return {
            'Authorization': 'Token %s' % self.api_key,
            'X-Secret': self.secret_key,
        }

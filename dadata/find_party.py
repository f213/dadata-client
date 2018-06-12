# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from dadata.base_client import DadataBaseClient


class DadataFindPartyClient(DadataBaseClient):
    """DaData find party client."""

    API_URL = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party'

    def request(self, query):
        """Send request to find-party API and return result data if
        provided."""
        return super(DadataFindPartyClient, self).request({'query': query})

    def _prepare_response(self, respose):
        try:
            return super(DadataFindPartyClient, self) \
                ._prepare_response(respose)['suggestions'] or None
        except (IndexError, KeyError, TypeError):
            return

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from dadata.base_client import DadataBasePaidClient


class DadataAddressStandartizationClient(DadataBasePaidClient):
    """DaData address standartization client."""

    API_URL = 'https://dadata.ru/api/v2/clean/address'

    def request(self, source):
        """Send request to standartization API and return result data if
        provided."""
        return super(DadataAddressStandartizationClient, self).request([source])

    def _prepare_response(self, respose):
        try:
            return super(DadataAddressStandartizationClient, self) \
                ._prepare_response(respose)[0] or None
        except (IndexError, KeyError):
            return

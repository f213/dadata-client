import requests
from dadata.exceptions import DadataPaymentRequired


class DadataFindPartyClient:
    """DaData find party client."""

    API_URL = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party'

    def __init__(self, key):
        self.api_key = key

    def _request_header(self):
        return {
            'Authorization': 'Token %s' % self.api_key,
        }

    def request(self, query):
        """Send request to find-party API and return result data if
        provided."""
        try:
            response = requests.post(
                self.API_URL,
                headers=self._request_header(),
                json={'query': query},
            )
        except requests.exceptions.ConnectTimeout:
            return

        return self._prepare_response(response)

    def _prepare_response(self, respose):
        if respose.status_code == 402:
            raise DadataPaymentRequired()

        if respose.status_code == 200:
            try:
                return respose.json()['suggestions'] or None
            except (IndexError, KeyError, TypeError):
                return

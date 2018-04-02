import requests


class DadataPaymentRequired(BaseException):
    pass


class DadataAddressStandartizationClient:
    """DaData address standartization client."""

    API_URL = 'https://dadata.ru/api/v2/clean/address'

    def __init__(self, key, secret):
        self.api_key = key
        self.secret_key = secret

    def _request_header(self):
        return {
            'Authorization': 'Token %s' % self.api_key,
            'X-Secret': self.secret_key,
        }

    def request(self, source):
        """Send request to standartization API and return result data if
        provided."""
        try:
            response = requests.post(self.API_URL, headers=self._request_header(), json=[source])
        except requests.exceptions.ConnectTimeout:
            return

        return self._prepare_response(response)

    def _prepare_response(self, respose):
        if respose.status_code == 402:
            raise DadataPaymentRequired()

        if respose.status_code == 200:
            try:
                return respose.json()[0] or None
            except (IndexError, KeyError):
                return

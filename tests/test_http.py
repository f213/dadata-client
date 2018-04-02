import requests

import pytest


def test_ok(client, response):
    client.http_mock.post('https://dadata.ru/api/v2/clean/address', json=response('ok'))

    got = client.request('Magadan,  Former Communism builders street, 5')

    assert got['postal_code'] == '127642'


def test_credentials(client, response):
    def _test_credentials(request, context):
        assert request.headers['Authorization'] == 'Token h4xxx0r'
        assert request.headers['X-Secret'] == 'z3r0c001'

        return response('ok')

    client.http_mock.post('https://dadata.ru/api/v2/clean/address', json=_test_credentials)

    client.request('Magadan,  Former Communism builders street, 5')


def test_timeout(client):
    client.http_mock.post('https://dadata.ru/api/v2/clean/address', exc=requests.exceptions.ConnectTimeout)

    got = client.request('Magadan,  Former Communism builders street, 5')

    assert got is None


def test_non_timeout_exceptions_are_propagated(client):
    client.http_mock.post('https://dadata.ru/api/v2/clean/address', exc=requests.exceptions.SSLError)
    with pytest.raises(requests.exceptions.SSLError):
        client.request('Magadan,  Former Communism builders street, 5')


def test_empty_response(client):
    client.http_mock.post('https://dadata.ru/api/v2/clean/address', json=[])

    got = client.request('Magadan,  Former Communism builders street, 5')

    assert got is None

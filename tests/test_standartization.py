# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import requests
import requests_mock

from dadata.exceptions import DadataPaymentRequired
from dadata.standartization import DadataAddressStandartizationClient


@pytest.fixture
def client():
    client = DadataAddressStandartizationClient(key='h4xxx0r', secret='z3r0c001')
    with requests_mock.Mocker() as http_mock:
        client.http_mock = http_mock
        yield client


@pytest.fixture
def response(read_fixture):
    return read_fixture('standartization_ok')


def test_ok(client, response):
    client.http_mock.post('https://dadata.ru/api/v2/clean/address', json=response)

    got = client.request('Magadan,  Former Communism builders street, 5')

    assert got['postal_code'] == '127642'


def test_credentials(client, response):
    def _test_credentials(request, context):
        assert request.headers['Authorization'] == 'Token h4xxx0r'
        assert request.headers['X-Secret'] == 'z3r0c001'

        return response

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


def test_payment_required(client):
    client.http_mock.post('https://dadata.ru/api/v2/clean/address', status_code=402)

    with pytest.raises(DadataPaymentRequired):
        client.request('Magadan,  Former Communism builders street, 5')

import pytest
import requests
import requests_mock

from dadata.exceptions import DadataPaymentRequired
from dadata.find_party import DadataFindPartyClient


@pytest.fixture
def client():
    client = DadataFindPartyClient(key='h4xxx0r')
    with requests_mock.Mocker() as http_mock:
        client.http_mock = http_mock
        yield client


@pytest.fixture
def response(read_fixture):
    return read_fixture('find_party_ok')


@pytest.mark.parametrize('query', (
    '7707083893',  # inn only
    'ПАО СБЕРБАНК',  # name only
    '1027700132195',  # ogrn only
    '7707083893 1027700132195 ПАО СБЕРБАНК',  # inn, ogrn and name
))
def test_ok(query, client, response):
    client.http_mock.post(
        'https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party',
        json=response,
    )

    got = client.request(query)[0]

    assert got['value'] == 'ПАО СБЕРБАНК'
    assert got['data']['inn'] == '7707083893'
    assert got['data']['ogrn'] == '1027700132195'


def test_credentials(client, response):
    def _test_credentials(request, context):
        assert request.headers['Authorization'] == 'Token h4xxx0r'

        return response

    client.http_mock.post(
        'https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party',
        json=_test_credentials,
    )

    client.request('7707083893')


def test_timeout(client):
    client.http_mock.post(
        'https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party',
        exc=requests.exceptions.ConnectTimeout,
    )

    got = client.request('7707083893')

    assert got is None


def test_non_timeout_exceptions_are_propagated(client):
    client.http_mock.post(
        'https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party',
        exc=requests.exceptions.SSLError,
    )
    with pytest.raises(requests.exceptions.SSLError):
        client.request('7707083893')


@pytest.mark.parametrize('json', (
    [],
    {},
    {'suggestions': []},
))
def test_empty_response(json, client):
    client.http_mock.post(
        'https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party',
        json=json,
    )

    got = client.request('7707083893')

    assert got is None


def test_payment_required(client):
    client.http_mock.post(
        'https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party',
        status_code=402,
    )

    with pytest.raises(DadataPaymentRequired):
        client.request('7707083893')

import json
from os import path

import pytest
import requests_mock
from dadata.standartization import DadataAddressStandartizationClient


@pytest.fixture
def client():
    """Configured instance of scrapyc"""
    client = DadataAddressStandartizationClient(key='h4xxx0r', secret='z3r0c001')
    with requests_mock.Mocker() as http_mock:
        client.http_mock = http_mock
        yield client


@pytest.fixture
def response():
    """Fixture reader"""
    def read_file(f):
        with open(path.join('tests/fixtures/', f) + '.json') as fp:
            return json.load(fp)

    return read_file

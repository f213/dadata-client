# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from os import path

import pytest


@pytest.fixture
def read_fixture():
    """Fixture reader"""
    def read_file(f):
        with open(path.join('tests/fixtures/', f) + '.json') as fp:
            return json.load(fp)

    return read_file



import json
from pathlib import Path

import pytest
from jsonschema import validate

SCHEMA_NAME = 'tokenlist.schema.json'


@pytest.fixture()
def get_schema():
    with open(f'tests/{SCHEMA_NAME}') as f:
        return json.load(f)


@pytest.mark.parametrize('file', Path(Path().root).glob('*.json'))
def test_token_list_schema(file, get_schema):
    with open(file) as f:
        token_list = json.load(f)
        validate(token_list, get_schema)


@pytest.mark.parametrize('file', Path(Path().root).glob('*.json'))
def test_token_tag_in_tags_list(file):
    """Check that all tokens in the list have a tag in the tags list."""
    with open(file) as f:
        token_list = json.load(f)
        for token in token_list['tokens']:
            for tag in token['tags']:
                assert tag in token_list['tags']
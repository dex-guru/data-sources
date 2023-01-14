import json
from pathlib import Path

import pytest
from jsonschema import validate

SCHEMA_NAME_CHAINS = 'chains.schema.json'
SCHEMA_NAME_DAPPS = 'dapps.schema.json'


@pytest.fixture()
def get_schema_chains():
    with open(f'tests/{SCHEMA_NAME_CHAINS}') as f:
        return json.load(f)

@pytest.fixture()
def get_schema_dapps():
    with open(f'tests/{SCHEMA_NAME_DAPPS}') as f:
        return json.load(f)


@pytest.mark.parametrize('file', Path(Path().root).glob('*.json'))
def test_chains_schema(file, get_schema):
    with open(file) as f:
        cd_list = json.load(f)
        validate(cd_list, get_schema)


@pytest.mark.parametrize('file', Path(Path().root).glob('*.json'))
def test_token_tag_in_tags_list(file):
    """Check that all tokens in the list have a tag in the tags list."""
    with open(file) as f:
        cd_list = json.load(f)
        for token in cd_list['tokens']:
            for tag in token['tags']:
                assert tag in cd_list['tags']
# TODO: Rewrite
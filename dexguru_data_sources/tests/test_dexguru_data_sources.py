#!/usr/bin/env python

"""Test for `dexguru_config_package` package."""

import pytest

from dexguru_data_sources.dexguru_data_sources import get_client


class TestLocalAPIClient:
    def test_config(self):
        config = get_client()
        assert config

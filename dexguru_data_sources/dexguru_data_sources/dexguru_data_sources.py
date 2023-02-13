"""Main module."""
import os
import json
from abc import ABC
from typing import List, Optional

from pydantic import BaseSettings

from dexguru_data_sources.models.amm_inventory_model import BaseAmmModel
from dexguru_data_sources.models.chain_inventory_model import BaseChainModel


class UtilsConfig(BaseSettings):
    CONFIG_API_URL: Optional[str] = None
    CONFIG_API_TOKEN: Optional[str] = None


utils_config = UtilsConfig()


class APIClient(ABC):

    def get_chains(self) -> List[BaseChainModel]:
        raise NotImplementedError

    def get_dapps(self, chain_id: int) -> List[BaseAmmModel]:
        raise NotImplementedError


def get_client(api_token: Optional[str] = None) -> APIClient:
    return LocalAPIClient()


class LocalAPIClient(APIClient):
    def __init__(self):
        chains_result, dapps_result = self.scan_paths()
        self.chains_data = chains_result
        self.dapps_data = dapps_result
        self.chains_dictionary = self.get_chains()
        self.dapps_dictionary = self.get_dapps()

    def scan_paths(self):
        path_parent = os.path.dirname(os.getcwd())
        chains_path = f'{path_parent}/dexguru_data_sources/api_data/chains/evm'
        dapps_path = f'{path_parent}/dexguru_data_sources/api_data/dapps/evm'
        chains_scan = os.scandir(chains_path)
        dapps_scan = os.scandir(dapps_path)
        chains_result = []
        dapps_result = []
        for chain in chains_scan:
            iterate_scan = os.scandir(chain.path)
            for jsons in iterate_scan:
                with open(jsons.path) as iterate_json:
                    chains = json.load(iterate_json)
                    chains_result.append(chains)
        for dapp in dapps_scan:
            iterate_scan = os.scandir(dapp.path)
            for jsons_dapp in iterate_scan:
                with open(jsons_dapp.path) as iterate_json_dapp:
                    dapps = json.load(iterate_json_dapp)
                    dapps_result.append(dapps)
        return chains_result, dapps_result

    def get_chains(self):
        chains = []
        chains_dictionary = {}
        for chain in self.chains_data:
            if chain:
                chains.append(chain)
        for chain_list in chains:
            for dictionary in chain_list:
                chains_dictionary[dictionary['id']] = dictionary
        return chains_dictionary

    def get_dapps(self):
        dapps = []
        dapps_dictionary = {}
        for dapp in self.dapps_data:
            if dapp:
                dapps.append(dapp)
        for dapps_list in dapps:
            for dictionary_dapp in dapps_list:
                string_int = '_' + str(dictionary_dapp['chain_id'])
                dapps_dictionary[dictionary_dapp['name'] + string_int] = dictionary_dapp
        return dapps_dictionary

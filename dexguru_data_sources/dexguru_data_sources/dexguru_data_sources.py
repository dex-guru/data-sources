"""Main module."""
import json
import os


def get_client():
    return EVMDataSources()


class EVMDataSources:
    def __init__(self):
        iterated_chains, iterated_dapps = self.scan_paths()
        self.chains_jsons = iterated_chains
        self.dapps_jsons = iterated_dapps
        self.chains = self.get_chains()
        self.dapps = self.get_dapps()

    def scan_paths(self):
        path_parent = os.path.dirname(os.getcwd())
        main_parent = os.path.dirname(path_parent)
        chains_path = f'{main_parent}/chains/evm'
        dapps_path = f'{main_parent}/dapps/evm'
        chains_scan = os.scandir(chains_path)
        dapps_scan = os.scandir(dapps_path)
        iterated_chains = []
        iterated_dapps = []
        for chain in chains_scan:
            iterate_scan = os.scandir(chain.path)
            for jsons in iterate_scan:
                with open(jsons.path) as iterate_json:
                    chains = json.load(iterate_json)
                    iterated_chains.append(chains)
        for dapp in dapps_scan:
            iterate_scan = os.scandir(dapp.path)
            for jsons_dapp in iterate_scan:
                with open(jsons_dapp.path) as iterate_json_dapp:
                    dapps = json.load(iterate_json_dapp)
                    iterated_dapps.append(dapps)
        return iterated_chains, iterated_dapps

    def get_chains(self):
        chains_list = []
        chains_dictionary = {}
        for chain in self.chains_jsons:
            if chain:
                chains_list.append(chain)
        for chain_list in chains_list:
            for dictionary in chain_list:
                chains_dictionary[dictionary['id']] = dictionary
        return chains_dictionary

    def get_dapps(self):
        dapps_list = []
        dapps_dictionary = {}
        for dapp in self.dapps_jsons:
            if dapp:
                dapps_list.append(dapp)
        for dapps_list in dapps_list:
            for dictionary_dapp in dapps_list:
                string_int = '_' + str(dictionary_dapp['chain_id'])
                dapps_dictionary[dictionary_dapp['name'] + string_int] = dictionary_dapp
        return dapps_dictionary

from dexguru_data_sources.dexguru_data_sources import get_client, utils_config

api_client = get_client(url=utils_config.CONFIG_API_URL, api_token=utils_config.CONFIG_API_TOKEN)

AmmChoices = api_client.get_amm_choices()
AmmIDChoices = api_client.get_amm_id_choices()
NetworkChoices = api_client.get_network_choices()
ChainChoices = api_client.get_chain_choices()
NativeTokenAddresses = api_client.get_native_token_addresses()

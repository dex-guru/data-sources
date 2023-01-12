# Dex.guru Data Sources
Dex.guru indexes chains and market aggregators to get the most accurate data possible. Our indexation works through a
configuration system with multiple JSONs for configs.

Under the chains folder are the current configs for chains, with folders inside chains/evm named for their chain id 
(Ethereum = 1, Polygon = 137, BSC = 56, etc.)

Under the dapps folder, in dapps/evm, are dapps/AMMs/market aggregators, sorted by type of AMM 
(ex: AMMs running on uniswap_v2 go under uniswap_v2)

If you want to add a chain, aggregator or AMM to dex.guru's indexation, you can fill in the details with the same template as the 
JSON you're editing and submit a merge request

Examples:
```json
  {
    "chain_id": 137,
    "name": "fakeswap",
    "type": "uniswap_v2",
    "enabled": true,
    "contracts": {
      "UniswapV2Router": "0x0",
      "UniswapV2Factory": "0x0"
    }
  }
```
```json
  {
    "id": 1337,
    "name": "fakechain",
    "type": "evm",
    "enabled": true,
    "native_token_address": "0x0",
    "native_token": {
      "address": "0x0",
      "name": "Wrapped Fakes",
      "symbol": "WFAKE",
      "decimals": 18
    },
    "stablecoin_addresses": [
      "0x0",
      "0x0",
      "0x0"    
    ]
  }
```
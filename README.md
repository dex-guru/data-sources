# Dex.guru Data Sources 

Dex.guru indexes chains and market aggregators to get the most accurate data possible. Our indexation works through a
configuration system with multiple JSONs for configs.

Under the chains folder are the current configs for chains, with folders inside chains/evm named for their chain id 
(Ethereum = 1, Polygon = 137, BSC = 56, etc.)

Under the dapps folder, in dapps/evm, are dapps/AMMs/market aggregators, sorted by type of AMM 
(ex: AMMs running on uniswap_v2 go under uniswap_v2)


# Chains Integration

Chains integration starts from submitting of chain config in current repo, and being picked up by developers team
at PR stage. After submitting the PR please contact us at [Discord](https://discord.com/channels/779159507967672360/928096490134573087), so we would be able
to figure out infrastructure/metadata (names, logos) questions before getting into staging and production environments (merging the PR).

ETH Chain config example:
```json
[
  {
    "id": 1,
    "name": "eth",
    "type": "evm",
    "enabled": true,
    "native_token_address": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
    "native_token": {
      "address": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
      "name": "Wrapped Ether",
      "symbol": "WETH",
      "decimals": 18
    },
    "stablecoin_addresses": [
      "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
      "0xdac17f958d2ee523a2206206994597c13d831ec7",
      "0x6b175474e89094c44da98b954eedeac495271d0f",
      "0x0000000000085d4780b73119b644ae5ecd22b376",
      "0x4fabb145d64652a948d72533023f6e7a623c7c53",
      "0x8e870d67f660d95d5be530380d0ec0bd388289e1",
      "0x956F47F50A910163D8BF957Cf5846D573E7f87CA",
      "0x853d955aCEf822Db058eb8505911ED77F175b99e",
      "0xBC6DA0FE9aD5f3b0d58160288917AA56653660E9",
      "0x57Ab1ec28D129707052df4dF418D58a2D46d5f51",
      "0x5f98805A4E8be255a32880FDeC7F6728C6568bA0",
      "0x674C6Ad92Fd080e4004b2312b45f796a192D27a0"
    ]
  }
]
```

# Dapps (currently AMMs) Integration

Dapps are divided by chain type (currenlty it's evm only), and dapp type. For example if you have an AMM you want to add
to dex.guru and it's fork, by means of parsed SWAP/BURNS/MINTS/SYNC events, of Uniswap V2, you would add it to the uniswap_v2 folder. 
After submitting the PR please contact us at [Discord](https://discord.com/channels/779159507967672360/928096490134573087), so we would be able 
to add metadata/logos to the dapp, otherwise it would be indexed and shown on dex.guru with default Unknown branding after
merging to main and deploying to dex.guru staging and production envs.


AMM config example:
```json
[
  {
    "chain_id": 1,
    "name": "uniswap",
    "type": "uniswap_v2",
    "enabled": true,
    "contracts": {
      "UniswapV2Router": "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D",
      "UniswapV2Factory": "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
    }
  },
  {
    "chain_id": 1,
    "name": "sushiswap",
    "type": "uniswap_v2",
    "enabled": true,
    "contracts": {
      "UniswapV2Router": "0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F",
      "UniswapV2Factory": "0xC0AEe478e3658e2610c5F7A4A2E1777cE9e4f2Ac"
    }
  },

```
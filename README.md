# DexGuru Data Sources 

At DexGuru, we are dedicated to providing the most accurate and up-to-date information on on-chain markets and asset movements. Our indexation pipeline is a robust system that utilizes multiple JSON configurations to ensure accuracy and reliability. However, we understand that the process of adding new data sources, such as new blockchains and decentralized exchanges, can be complex and opaque. That's why we are committed to streamlining and simplifying this process to make it more transparent and open to the community. With this approach, we aim to empower defi community to have better access to the latest information and trends in on-chain data space.

## Repo Structure
Under the chains folder are the current configs for chains, with folders inside chains/evm named for their [chain id](https://chainlist.org/) 
(Ethereum = 1, Polygon = 137, BSC = 56, etc.)

Under the dapps folder, in dapps/evm, are dapps/AMMs/market, sorted by type of AMM 
(ex: AMMs running on uniswap_v2 or Uniiswap v2 forks goes under uniswap_v2).  

Further reading: 
>   - [Data FAQ at our Gitbook](https://docs.dex.guru/data/data-faq)
>   - [Supported Markets](https://dex.guru/markets)
>   - [Off-chain data usage](https://docs.dex.guru/data/off-chain-data-usage)


# New Blockchain Integration

Blockchain integration starts from submitting of chain config in a current repo, and being picked up by developers team at PR stage. 

### New Blockchain Submissions:
We'll need the following to integrate your **EVM-compatible** blockchain: 

- [ ] At least one AMM on your chain with a daily volume over $100k. Please include it in your PR.    
- [ ] Your chain logo. Add a link to a PR description or attach to a new issue in this repo. 
- [ ] You native token logo should be added at [assets repo](https://github.com/dex-guru/assets)  
- [ ] Link to your current [tokenlist](https://tokenlists.org/) by someone with a reputation. Unless there is a reputable site(s), e.g. Coingecko, supporting tokens from your chain, we will mark all tokens as [Degen mode](https://docs.dex.guru/data/off-chain-data-usage).  
- [ ] Blockexplorer that could open account and transaction pages. Please include a link in PR description or attach it to a new issue in this repo.   
- [ ] At least one stablecoin with **stable** price. Preferably native stablecoins(e.g. USDT) or their bridged versions. 
- [ ] High-performance RPC endpoint. This endpoint should be able to handle at least x3 of your chain average TX/block count per avg. block time. We strive to index data in real-time or as close to real-time as possible. Please raise the issue in this repo or reach out to our team at [Discord](https://discord.com/invite/dPW8fzwzz9) with access details.  


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

Dapps are divided by chain type (currently, it's evm only), and dapp type. For example, if you have an AMM you want to add to DexGuru and it's fork(using the same or similar smart contracts), by means of parsed SWAP/BURNS/MINTS/SYNC events, of Uniswap V2, you would add it to the uniswap_v2 folder. 

### New AMM Submissions:
We'll need the following to integrate your AMM: 
* [ ] Do you have a daily trading volume over $20k? 
* [ ] Does "type" at AMM config match your code base? 
* [ ] Your AMM logo. Please add a link to your logo or attach it to a new issue in this repo.  
 
 
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

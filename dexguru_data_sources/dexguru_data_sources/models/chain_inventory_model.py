from typing import Optional, List

from pydantic import constr, PositiveInt

from .base_model import BaseModelDexGuru
from .token_inventory import TokenInventoryStatic
from .values import address


class ChainId(BaseModelDexGuru):
    value: PositiveInt = 1


class BaseChainModel(BaseModelDexGuru):
    chain_id: PositiveInt = 1
    name: constr(strict=True, min_length=0, max_length=50, strip_whitespace=True) = ''
    type: constr(strict=True, min_length=0, max_length=50, strip_whitespace=True) = ''
    enabled: bool = True
    native_token_address: address = ''
    native_token: Optional[TokenInventoryStatic] = None
    stablecoin_addresses: List[str] = []

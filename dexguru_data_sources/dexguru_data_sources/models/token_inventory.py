from typing import Optional

from pydantic import constr, conint

from .base_model import BaseModelDexGuru
from .values import address

SUPPORTED_TRANSACTION_TYPES = []
SUPPORTED_AMM_LIST = []
SUPPORTED_NETWORK_LIST = []


class TokenInventoryStatic(BaseModelDexGuru):
    """ Not modified fields of TokenInventory """
    id: constr(strip_whitespace=True)
    address: address
    name: constr(strict=True, min_length=1, max_length=50, strip_whitespace=True)
    symbol: constr(strict=True, min_length=1, max_length=50, strip_whitespace=True)
    logo_uri: Optional[str] = None
    decimals: conint(ge=0) = 0
    chain_id: Optional[int] = None

from pydantic import constr, PositiveInt

from .base_model import BaseModelDexGuru

"""
    New Amm models are devided into Backend and Frontend parts
    BackendModel key: BackendAmmModel:id-1, mset
    MetadataAmmModel key: MetadataAmmModel:id-2
"""


class BaseAmmModel(BaseModelDexGuru):
    chain_id: PositiveInt
    name: constr(strict=True, min_length=1, max_length=50, strip_whitespace=True) = ''
    type: constr(strict=True, min_length=1, max_length=50, strip_whitespace=True) = ''
    enabled: bool = False
    contracts: dict = {}

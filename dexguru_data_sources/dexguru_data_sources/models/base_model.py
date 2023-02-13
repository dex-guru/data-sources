from pydantic import BaseModel


class BaseModelDexGuru(BaseModel):
    class Config:
        # check types on set/update
        validate_assignment = True
        validate_all = True
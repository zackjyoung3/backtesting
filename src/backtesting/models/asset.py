from pydantic import BaseModel

from backtesting.enums import AssetType


class Asset(BaseModel):
    ticker: str
    type: AssetType

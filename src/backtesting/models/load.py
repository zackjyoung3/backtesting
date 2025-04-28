from datetime import date

from pydantic import BaseModel, conlist

from backtesting.enums import TimeUnit
from backtesting.models.asset import Asset


class AssetInfoLoadRequest(BaseModel):
    """
    Request model for loading asset information for backtesting.

    For any specified target interval (e.g., 15 minutes), data is retrieved at the highest available granularity
    (currently one-minute intervals) to maximize the number of constructed testing windows.
    This ensures stable, high-resolution backtesting.

    In the future, retrieval strategies may be extended to support coarser or dynamic granularities
    (e.g., hourly sampling for daily intervals). But that is beyond the Request Models concerns.
    """

    assets: conlist(Asset, min_length=1)
    granularity_level: TimeUnit
    start_date: date
    end_date: date

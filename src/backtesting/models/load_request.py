from datetime import date
from typing import Self

from pydantic import BaseModel, conlist, model_validator

import backtesting.constants as C
from backtesting.enums import TimeUnit
from backtesting.models.asset import Asset
from backtesting.utils import time_ext


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

    @model_validator(mode="after")
    def validate_start_le_end(self) -> Self:
        if self.start_date > self.end_date:
            raise ValueError(f"start_date must be before end_date, have {self}")
        return self

    @model_validator(mode="after")
    def validate_dates_correct_for_granularity(self) -> Self:
        if self.granularity_level in time_ext.INTRADAY_UNITS:
            return self  # from validate_start_le_end, we have at least 1 day => can always fulfill intraday
        one_unit_after_start = time_ext.advance_time(self.start_date, self.granularity_level, C.SINGLE_UNIT_QUANTITY)
        if one_unit_after_start > self.end_date:
            raise ValueError(f"Start date advanced by one unit would be after end date for {self}")
        return self

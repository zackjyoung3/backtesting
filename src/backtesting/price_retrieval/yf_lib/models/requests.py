"""
yf_lib.models.requests

Only model subset of requests to yfinance that we want our application to support
"""

from abc import ABC
from datetime import date
from typing import Any, Self

from pydantic import BaseModel

from backtesting.price_retrieval.yf_lib.interval import YfTimeInterval
from backtesting.price_retrieval.yf_lib.period import YfPeriod


class YfRequestBase(BaseModel, ABC):
    tickers: str | list[str]
    interval: YfTimeInterval

    def model_dump_kwargs(self) -> dict[str, Any]:
        """dumps the model out as kwargs compatible with yfinance.download kwargs"""
        return self.model_dump(mode="json")


class YfPeriodRequest(YfRequestBase):
    period: YfPeriod


class YfDateRangeRequest(YfRequestBase):
    start: date
    end: date

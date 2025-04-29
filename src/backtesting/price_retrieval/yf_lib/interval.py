"""
yf_lib.interval

TimeInterval: Present unified enum for all possible values that an interval can take on in yfinance
    - Although minute + non-minute time unit intervals could be separated into diff classes, logically easier
      for usability to have single enum that represents all valid time intervals
"""

from enum import StrEnum
from typing import Self

from backtesting.enums import TimeUnit


class YfTimeInterval(StrEnum):
    """Supported time intervals for yfinance requests that can be serviced by our application"""

    ONE_MINUTE = "1m"
    ONE_HOUR = "1h"
    ONE_DAY = "1d"
    ONE_WEEK = "1wk"
    ONE_MONTH = "1mo"

    @classmethod
    def for_time_unit(cls, time_unit: TimeUnit) -> Self:
        match time_unit:
            case TimeUnit.MINUTES:
                return cls.ONE_MINUTE
            case TimeUnit.HOURS:
                return cls.ONE_HOUR
            case TimeUnit.DAYS:
                return cls.ONE_DAY
            case TimeUnit.WEEKS:
                return cls.ONE_WEEK
            case TimeUnit.MONTHS:
                return cls.ONE_MONTH
            case TimeUnit.YEARS:
                return cls.ONE_MONTH  # yfinance does not have 1y interval => use month
            case _:
                raise ValueError(f"Time Unit has no supported interval in yfinance {time_unit}")

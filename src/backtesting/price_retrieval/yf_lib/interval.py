"""
yf_lib.interval

TimeInterval: Present unified enum for all possible values that an interval can take on in yfinance
    - Although minute + non-minute time unit intervals could be separated into diff classes, logically easier
      for usability to have single enum that represents all valid time intervals
"""

from enum import StrEnum


class YfTimeInterval(StrEnum):
    """Supported time intervals by yfinance"""

    # in minutes
    ONE_MINUTE = "1m"
    TWO_MINUTES = "2m"
    FIVE_MINUTES = "5m"
    FIFTEEN_MINUTES = "15m"
    THIRTY_MINUTES = "30m"
    SIXTY_MINUTES = "60m"
    NINETY_MINUTES = "90m"

    # in non-minute time units
    ONE_HOUR = "1h"
    ONE_DAY = "1d"
    FIVE_DAYS = "5d"
    ONE_WEEK = "1wk"
    ONE_MONTH = "1mo"
    THREE_MONTHS = "3mo"

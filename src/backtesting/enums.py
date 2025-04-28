from enum import IntEnum, StrEnum


class AssetType(StrEnum):
    """Asset types that are in scope for this project"""

    EQUITY = "EQUITY"
    CRYPTO = "CRYPTO"
    COMMODITY = "COMMODITY"


class TimeUnit(StrEnum):
    """Different time units that are going to be supported in terms of granularity for intervals"""

    SECONDS = "SECONDS"
    MINUTES = "MINUTES"
    HOURS = "HOURS"
    DAYS = "DAYS"
    WEEKS = "WEEKS"
    MONTHS = "MONTHS"
    YEARS = "YEARS"


class TimeConversionMultiplier(IntEnum):
    """Only the standard time conversion multiplier e.g. to perform a single hop between units"""

    IDENTITY = 1
    SECONDS_IN_A_MINUTE = 60
    MINUTES_IN_AN_HOUR = 60
    HOURS_IN_A_DAY = 24
    DAYS_IN_A_WEEK = 7
    MONTHS_IN_A_YEAR = 12

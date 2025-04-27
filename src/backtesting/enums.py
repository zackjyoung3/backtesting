from enum import IntEnum


class TimeConversionMultiplier(IntEnum):
    """Only the standard time conversion multiplier e.g. to perform a single hop between units"""

    IDENTITY = 1
    SECONDS_IN_A_MINUTE = 60
    MINUTES_IN_AN_HOUR = 60
    HOURS_IN_A_DAY = 24
    DAYS_IN_A_WEEK = 7
    MONTHS_IN_A_YEAR = 12

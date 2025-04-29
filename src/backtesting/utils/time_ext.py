from datetime import date, datetime, timedelta

from dateutil.relativedelta import relativedelta

from backtesting.enums import TimeUnit

INTRADAY_UNITS = frozenset([TimeUnit.SECONDS, TimeUnit.MINUTES, TimeUnit.HOURS])


def advance_time(current_date: date | datetime, time_unit: TimeUnit, advance_quantity: int) -> date | datetime:
    """
    Advance a date or datetime by a specified quantity of time units. (If datetime.date passed and time unit less than
    a day => that date.datetime from start of the day + time change returned)

    :param current_date: The starting date or datetime.
    :param time_unit: The unit of time to advance (e.g., seconds, minutes, hours, days, months, years).
    :param advance_quantity: The number of units to advance (can be negative for moving backward).
    :return: A  new date or datetime object advanced by the specified amount.
    """
    if isinstance(current_date, date) and not isinstance(current_date, datetime) and time_unit in INTRADAY_UNITS:
        current_date = datetime.combine(current_date, datetime.min.time())

    match time_unit:
        case TimeUnit.SECONDS:
            advancement_addend = timedelta(seconds=advance_quantity)
        case TimeUnit.MINUTES:
            advancement_addend = timedelta(minutes=advance_quantity)
        case TimeUnit.HOURS:
            advancement_addend = timedelta(hours=advance_quantity)
        case TimeUnit.DAYS:
            advancement_addend = timedelta(days=advance_quantity)
        case TimeUnit.WEEKS:
            advancement_addend = timedelta(weeks=advance_quantity)
        case TimeUnit.MONTHS:
            advancement_addend = relativedelta(months=advance_quantity)
        case TimeUnit.YEARS:
            advancement_addend = relativedelta(years=advance_quantity)
        case _:
            raise ValueError(f"Unsupported Time Unit {time_unit}")
    return current_date + advancement_addend

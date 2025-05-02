class YfResponseInvalidError(Exception):
    """
    There are cases when the yfinance lib will return an emtpy df rather than telling you that the
    time interval + period specified in a request is invalid. In such cases, this error should be raised
    """

    pass

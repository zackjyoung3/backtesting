"""
yf_lib.download

Custom code to wrap normal yfinance download. Mostly just so we can correctly raise in case where yfinance will
suppress error when the period in which prices should be obtained for is too large for interval supplied
"""

from types import MappingProxyType
from typing import Any

import numpy as np
import pandas as pd
import yfinance as yf

from backtesting.price_retrieval.yf_lib.enums import ResponseColName
from backtesting.price_retrieval.yf_lib.error import YfResponseInvalidError
from backtesting.price_retrieval.yf_lib.models.requests import YfRequestBase


_COL_NAME_TO_TYPE_CONTRACT = MappingProxyType(
    {
        ResponseColName.LOW: np.float64,
        ResponseColName.HIGH: np.float64,
        ResponseColName.OPEN: np.float64,
        ResponseColName.CLOSE: np.float64,
        ResponseColName.VOLUME: np.int64,
    }
)

_INDEX_DTYPE = pd.DatetimeTZDtype("ns", "UTC")


def validate_returned_data_schema(df: pd.DataFrame, request: YfRequestBase) -> None:
    mismatches = []

    def add_mismatch(col: str, expected: Any, actual: Any | None = None) -> None:
        mismatches.append(f"{col} Expected: {expected}, Actual: {actual}")

    if df.index.dtype != _INDEX_DTYPE:
        add_mismatch("index", _INDEX_DTYPE, df.index.dtype)

    for ticker in request.tickers:
        for col_name in ResponseColName:
            # raise key error here, would be dev error in which we have not accounted for a col in mapping
            expected_type = _COL_NAME_TO_TYPE_CONTRACT[col_name]
            if (col_name, ticker) not in df.columns:
                add_mismatch(f"{col_name}.{ticker}", expected_type)
            else:
                actual_type = df.dtypes[col_name][ticker]
                if actual_type != expected_type:
                    add_mismatch(f"{col_name}.{ticker}", expected_type, actual_type)
    if mismatches:
        formatted_mismatches = "\n\t".join(mismatches)
        raise YfResponseInvalidError(
            f"Schema for df returned resulted in the following mismatches:\n\t{formatted_mismatches}"
        )


def _is_any_data_for_ticker(df: pd.DataFrame, ticker: str) -> bool:
    for col_name in ResponseColName:
        if (col_name, ticker) in df.columns:
            if not df[(col_name, ticker)].isna().all():
                return True
    return False


def _validate_data_was_returned_for_request(df: pd.DataFrame, request: YfRequestBase) -> None:
    if df is None or df.empty:
        raise YfResponseInvalidError(
            f"No data was returned for request: {request}. "
            f"This likely indicates that the interval for the request was incompatible with the period in the request."
        )

    tickers_failed = []
    for ticker in request.tickers:
        if not _is_any_data_for_ticker(df, ticker):
            tickers_failed.append(ticker)
    if tickers_failed:
        raise YfResponseInvalidError(
            f"For request: {request}\nNo data was returned for tickers: {tickers_failed}.\nDf head: {df.head()}"
        )


def download_stock_info(request: YfRequestBase, validate_request_returned_data: bool = True) -> pd.DataFrame:
    """
    Download stock info using yfinance lib, ensures schema returned is exactly as expected so we have no surprises
    in downstream processing

    :param request: request defining what asset info should be retrieved from yfinance lib
    :param validate_request_returned_data: whether to ensure that all tickers returned data. E.g. turn this flag on
           when you are certain that request should return data (defaults to True)
    :return: df with all stock info
    """
    ticker_data_df = yf.download(**request.model_dump_kwargs())
    validate_returned_data_schema(ticker_data_df, request)

    if validate_request_returned_data:
        _validate_data_was_returned_for_request(ticker_data_df, request)

    return ticker_data_df

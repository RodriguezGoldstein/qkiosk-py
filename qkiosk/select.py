"""
Data selection and conversion utilities for QKiosk Python API.
"""

import pandas as pd

def select(df: pd.DataFrame, rows=None, cols=None) -> pd.DataFrame:
    """
    Subset a DataFrame by rows and/or columns.

    Args:
        df: pandas DataFrame to subset
        rows: row labels or boolean mask
        cols: column labels or list of columns
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError('select requires a pandas DataFrame')
    result = df
    if rows is not None:
        result = result.loc[rows]
    if cols is not None:
        result = result.loc[:, cols]
    return result

def to_df(data) -> pd.DataFrame:
    """
    Convert list of dicts or DataFrame-like to pandas DataFrame.

    Args:
        data: list of dicts or DataFrame
    """
    if isinstance(data, pd.DataFrame):
        return data
    try:
        return pd.DataFrame(data)
    except Exception as e:
        raise ValueError(f"Cannot convert to DataFrame: {e}")

def to_ts(df: pd.DataFrame, index: str = None) -> pd.DataFrame:
    """
    Convert DataFrame to time series by setting a date/time column as index.

    Args:
        df: pandas DataFrame
        index: column name to use as datetime index
    Returns:
        DataFrame with datetime index
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError('to_ts requires a pandas DataFrame')
    if index:
        ts = df.copy()
        ts[index] = pd.to_datetime(ts[index])
        ts = ts.set_index(index)
        return ts
    return df

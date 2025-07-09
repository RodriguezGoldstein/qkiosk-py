"""
Styling utilities for QKiosk Python API.
"""

import pandas as pd

def highlight(df: pd.DataFrame, mask, style: dict = None, axis: int = 0):
    """
    Highlight rows or values in the DataFrame based on a boolean mask.

    Args:
        df: pandas DataFrame
        mask: boolean Series or array same length as df rows or columns
        style: CSS style dict to apply
        axis: 0 to highlight rows, 1 for columns
    Returns:
        pandas Styler object
    """
    if style is None:
        style = {'background-color': 'yellow'}
    if not isinstance(df, pd.DataFrame):
        raise ValueError('highlight requires a pandas DataFrame')
    def _apply(x):
        return [style if m else {} for m in mask]
    return df.style.apply(_apply, axis=axis)

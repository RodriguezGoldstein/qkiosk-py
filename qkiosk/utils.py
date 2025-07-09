"""
Utility functions for date handling in QKiosk Python API.
"""
import datetime

def today() -> int:
    """
    Return current date as YYYYMMDD integer.
    """
    return int(datetime.date.today().strftime("%Y%m%d"))

def yyyymmdd(x=None):
    """
    Convert input to YYYYMMDD integer. Accepts int, date, datetime, or None.
    """
    if x is None:
        return today()
    if isinstance(x, (datetime.date, datetime.datetime)):
        return int(x.strftime("%Y%m%d"))
    if isinstance(x, int) and len(str(x)) == 8:
        return x
    raise ValueError("x must be a date, datetime, or YYYYMMDD integer")

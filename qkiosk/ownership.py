"""
Ownership endpoints for QKiosk Python API.
"""
from .config import get_api_key

import time
import pandas as pd
import requests

from .config import get_api_key

def beneficial(qkid, yyyyqq, qtrs=1, form="13D13G", wait=1, quiet=True, as_json=False):
    """
    Retrieve beneficial ownership data (13D/13G) for a given QKID and quarter.
    """
    api_key = get_api_key()
    yyyy = str(yyyyqq)[:4]
    qq = str(yyyyqq)[4:]
    url = (
        f"https://api.qkiosk.io/data/ownership?form={form}"
        f"&apiKey={api_key}&ids={qkid.split('.')[0]}"
        f"&aggType=a&yyyy={yyyy}&qq={qq}&by=filing&retType=csv"
    )
    if not quiet:
        print(f'GET {url}')
    resp = requests.get(url)
    resp.raise_for_status()
    import io
    df = pd.read_csv(io.StringIO(resp.text))
    if as_json:
        return df.to_dict(orient='records')
    return df

def insider(qkid, yyyyqq, qtrs=1, form="345", wait=1, quiet=True, as_json=False):
    """
    Retrieve insider ownership data (Form 345) for a QKID and quarter.
    """
    api_key = get_api_key()
    yyyy = str(yyyyqq)[:4]
    qq = str(yyyyqq)[4:]
    url = (
        f"https://api.qkiosk.io/data/ownership?form={form}"
        f"&apiKey={api_key}&ids={qkid.split('.')[0]}"
        f"&aggType=a&yyyy={yyyy}&qq={qq}&by=filing&retType=csv"
    )
    if not quiet:
        print(f'GET {url}')
    resp = requests.get(url)
    resp.raise_for_status()
    import io
    df = pd.read_csv(io.StringIO(resp.text))
    if as_json:
        return df.to_dict(orient='records')
    return df

def holders(qkid, yyyyqq, qtrs=1, wait=1, quiet=True, as_json=False):
    """
    Retrieve institutional holders details for a QKID and quarter.
    """
    api_key = get_api_key()
    yyyy = str(yyyyqq)[:4]
    qq = str(yyyyqq)[4:]
    url = (
        f"https://api.qkiosk.io/data/instrument?apiKey={api_key}"
        f"&id={qkid.split('.')[0]}&yyyy={yyyy}&qq={qq}&id2=1974"
    )
    if not quiet:
        print(f'GET {url}')
    resp = requests.get(url)
    resp.raise_for_status()
    import io
    df = pd.read_csv(io.StringIO(resp.text))
    if as_json:
        return df.to_dict(orient='records')
    return df

def institutional(qkid, yyyyqq, qtrs=1, agg=True, wait=0, quiet=True, as_json=False):
    """
    Retrieve aggregated institutional ownership data for a QKID and quarter.
    """
    api_key = get_api_key()
    yyyy = str(yyyyqq)[:4]
    qq = str(yyyyqq)[4:]
    aggType = 'a' if agg else 'n'
    url = (
        f"https://api.qkiosk.io/data/ownership?apiKey={api_key}&ids={qkid.split('.')[0]}"
        f"&aggType={aggType}&yyyy={yyyy}&qq={qq}&by=filing&retType=csv"
    )
    if not quiet:
        print(f'GET {url}')
    resp = requests.get(url)
    resp.raise_for_status()
    import io
    df = pd.read_csv(io.StringIO(resp.text))
    if as_json:
        return df.to_dict(orient='records')
    return df

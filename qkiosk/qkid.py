"""
QKID conversion utilities for QKiosk Python API.
"""

import re
import io
import pandas as pd
import requests

from .config import get_api_key

_QKID_REGEX = re.compile(
    r"([0-9]{10})[.]([A-Z0-9]{4})[.]([BCDFGHJKLMNPQRSTVWXYZ0-9]{9})|"
    r"([0-9]{10})[.]([A-Z0-9]{4})[.](UF[CDFGHJKLMNPQRSTVWXYZ0-9]{6}[A])"
)

_MAPPING_CACHE = {}

def _load_mapping(id_type: str) -> pd.DataFrame:
    """
    Load and cache the full mapping table for a given identifier type.
    """
    if id_type not in _MAPPING_CACHE:
        _MAPPING_CACHE[id_type] = _req_qkid(id_type, id_type)
    return _MAPPING_CACHE[id_type]

def to_qkid(value: str) -> str:
    """
    Validate and return the QKID string if it matches expected pattern.
    """
    qkid = str(value)
    if _QKID_REGEX.fullmatch(qkid):
        return qkid
    raise ValueError(f"Invalid QKID format: {qkid}")

def qk_ticker(ticker: str) -> str:
    """
    Lookup the QKID corresponding to a ticker string (R's qk_ticker equivalent).
    """
    df = _load_mapping('ticker')
    if 'ticker' in df.columns and 'qkid' in df.columns:
        match = df.loc[df['ticker'] == ticker]
        if not match.empty:
            return match['qkid'].iloc[0]
    raise ValueError(f"No QKID found for ticker {ticker}")

def _req_qkid(id_type: str, ids: str) -> pd.DataFrame:
    """
    Internal helper to request QKID mappings for various identifier types.
    Returns a pandas DataFrame with columns including 'qkid' and the identifier.
    """
    api_key = get_api_key()
    url = "https://api.qkiosk.io/data/qkid"
    payload = {"apiKey": api_key, "ids": ids}
    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    data = resp.json()
    csv_url = data.get("Urls", [None])[0]
    if not csv_url:
        raise RuntimeError(f"No mapping URL returned for {id_type}")
    r = requests.get(csv_url)
    r.raise_for_status()
    return pd.read_csv(io.StringIO(r.text), dtype=str)

# --- Full identifier mapping functions (mirror R/qkid.R) ---
def qk_cik(cik: str) -> list:
    df = _load_mapping('cik')
    return df['qkid'].tolist()

def to_cik(qkid: str) -> str:
    df = _load_mapping('cik')
    match = df.loc[df['qkid'] == qkid]
    if not match.empty:
        return match['cik'].iloc[0]
    raise ValueError(f"No CIK found for QKID {qkid}")

def qk_figi(figi: str) -> list:
    df = _load_mapping('figi')
    return df['qkid'].tolist()

def to_figi(qkid: str) -> str:
    df = _load_mapping('figi')
    match = df.loc[df['qkid'] == qkid]
    if not match.empty:
        return match['figi'].iloc[0]
    raise ValueError(f"No FIGI found for QKID {qkid}")

def qk_permid(permid: str) -> list:
    df = _load_mapping('permid')
    return df['qkid'].tolist()

def to_permid(qkid: str) -> str:
    df = _load_mapping('permid')
    match = df.loc[df['qkid'] == qkid]
    if not match.empty:
        return match['permid'].iloc[0]
    raise ValueError(f"No PERMID found for QKID {qkid}")

def qk_name(name: str) -> list:
    df = _load_mapping('name')
    return df['qkid'].tolist()

def to_name(qkid: str) -> str:
    df = _load_mapping('name')
    match = df.loc[df['qkid'] == qkid]
    if not match.empty:
        return match['name'].iloc[0]
    raise ValueError(f"No name found for QKID {qkid}")

def qk_fundname(name: str) -> list:
    df = _load_mapping('fund')
    return df['qkid'].tolist()

def to_fundname(qkid: str) -> str:
    df = _load_mapping('fund')
    match = df.loc[df['qkid'] == qkid]
    if not match.empty:
        return match['fund'].iloc[0]
    raise ValueError(f"No fund name found for QKID {qkid}")

def qk_sector(sector: str) -> list:
    df = _load_mapping('sector')
    return df['qkid'].tolist()

def to_sector(qkid: str) -> str:
    df = _load_mapping('sector')
    match = df.loc[df['qkid'] == qkid]
    if not match.empty:
        return match['sector'].iloc[0]
    raise ValueError(f"No sector found for QKID {qkid}")

def qk_sic(sic: str) -> list:
    df = _load_mapping('sic')
    return df['qkid'].tolist()

def to_sic(qkid: str) -> str:
    df = _load_mapping('sic')
    match = df.loc[df['qkid'] == qkid]
    if not match.empty:
        return match['sic'].iloc[0]
    raise ValueError(f"No SIC found for QKID {qkid}")

# QKID component extraction and metadata
def entity(qkid: str) -> str:
    return qkid.split('.')[0]

def cls(qkid: str) -> str:
    return qkid.split('.')[1]

def instrument(qkid: str) -> str:
    return qkid.split('.')[2]

_QKIDCLASSMAP_V4 = {
    '0000': 'Equity', '000C': 'Equity (Call)', '000P': 'Equity (Put)',
    '0010': 'Warrant', '001C': 'Warrant (Call)', '001P': 'Warrant (Put)',
    '0020': 'Unit', '002C': 'Unit (Call)', '002P': 'Unit (Put)',
    '0030': 'Right', '003C': 'Right (Call)', '003P': 'Right (Put)',
    '0300': 'Convert', '0400': 'ADR', '040C': 'ADR (Call)', '040P': 'ADR (Put)',
    '0500': 'Fund', '050C': 'Fund (Call)', '050P': 'Fund (Put)',
    '0510': 'Closed End Fund', '051C': 'Closed End Fund (Call)', '051P': 'Closed End Fund (Put)',
    '0570': 'REIT', '057C': 'REIT (Call)', '057P': 'REIT (Put)',
    '0600': 'Partnership', '060C': 'Partnership (Call)', '060P': 'Partnership (Put)',
    '0210': 'Note', '0220': 'Debt', '0230': 'Debt (MTN)', '0ZZZ': 'Undefined'
}

def classname(qkid: str) -> str:
    c = cls(qkid)
    return _QKIDCLASSMAP_V4.get(c, '')

def qkid_version(qkid: str) -> int:
    return 4 if _QKID_REGEX.fullmatch(qkid) else None

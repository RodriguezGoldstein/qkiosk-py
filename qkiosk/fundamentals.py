"""
Fundamental data endpoints for QKiosk Python API.
"""
import io
import requests
import pandas as pd

from .config import get_api_key

def fundamentals(qkids, items, view='asof', ticker=True, hide=True,
                 quiet=True, cache=False, as_json=False):
    """
    Retrieve fundamental financial data for given QKIDs and items.

    Args:
        qkids: list of QKID strings (e.g. ['0000320193.0000.001S5N8V8'])
        items: list of item codes (e.g. ['SALE', 'EBIT'])
        view: 'asof', 'asfiled', or 'pit'
        ticker: include ticker in output (unused)
        hide: mask API key in logs (unused)
        quiet: suppress request logs
        cache: unused in Python client

    Returns:
        pandas.DataFrame combining all requested fundamentals
    """
    api_key = get_api_key()
    # build payload for POST
    ids = ','.join([str(qkid).split('.')[0] for qkid in qkids])
    payload = {
        'apiKey': api_key,
        'ids': ids,
        'items': ','.join(items),
        'view': view,
    }
    url = 'https://api.qkiosk.io/data/fundamental'
    if not quiet:
        print(f'POST {url} payload={payload}')
    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    data = resp.json()
    # fetch CSVs for each returned URL
    dfs = []
    for u in data.get('Urls', []):
        r = requests.get(u)
        r.raise_for_status()
        df = pd.read_csv(io.StringIO(r.text))
        dfs.append(df)
    if dfs:
        result = pd.concat(dfs, ignore_index=True)
    else:
        result = pd.DataFrame()
    if as_json:
        return result.to_dict(orient='records')
    return result

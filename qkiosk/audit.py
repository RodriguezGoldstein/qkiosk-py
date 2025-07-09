"""
Audit endpoints for QKiosk Python API.
"""
import webbrowser
import requests

from .config import get_api_key

def audit(df, row=None, accn=None, fpe=None, open_browser=False, context=1):
    """
    Perform financial audit display for a selected DataFrame row.

    Returns a dict with 'stmt' (text) and 'url'.
    """
    api_key = get_api_key()
    if row is None:
        raise ValueError('row index must be specified')
    rec = df.loc[row]
    cik = rec.get('cik')
    accn = rec.get('accn')
    stmt = rec.get('stmt')
    concept_id = rec.get('concept_id')
    req_param = f"{accn}-{stmt}+hash.txt"
    url = (
        f"https://api.qkiosk.io/data/audit?id={cik}&req={req_param}"
        f"&prd=audit/fn/stmt&apiKey={api_key}"
    )
    resp = requests.get(url)
    resp.raise_for_status()
    lines = resp.text.splitlines()
    if open_browser:
        webbrowser.open(url)
    return {'stmt': '\n'.join(lines), 'url': url}

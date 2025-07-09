"""
Bulk filings download endpoint for QKiosk Python API.
"""
import os
import zipfile
import requests

from .config import get_api_key

def complete(dir_path, subscription='raw', rollup='5m', last='5m', date=None,
             fmt='zip', gzip=True, hide=True, quiet=False, force=False):
    """
    Download bulk filings into a local directory, unzip, and optionally gzip files.
    """
    api_key = get_api_key()
    date_str = date or ''
    url = (
        f"https://api.qkiosk.io/data/filings?fmt={fmt}&subscription={subscription}"
        f"&rollup={rollup}&date={date_str}&last={last}&apiKey={api_key}"
    )
    if not quiet:
        print(f'GET {url}')
    resp = requests.get(url)
    resp.raise_for_status()
    res = resp.json()

    out_dir = os.path.abspath(dir_path)
    os.makedirs(out_dir, exist_ok=True)

    downloads = []
    filings = []
    for file_url in res.get('Urls', []):
        filename = res.get('Filings', [])[res.get('Urls', []).index(file_url)]
        downloads.append(filename)
        target = os.path.join(out_dir, filename)
        if not force and os.path.exists(target):
            continue
        rfile = requests.get(file_url)
        rfile.raise_for_status()
        with open(target, 'wb') as f:
            f.write(rfile.content)
        if fmt == 'zip':
            with zipfile.ZipFile(target, 'r') as zf:
                zf.extractall(out_dir)
                filings.extend(zf.namelist())
    return {'downloads': downloads, 'filings': filings, 'directory': out_dir}

"""
Account endpoints for QKiosk Python API.
"""
import webbrowser
import requests

from .config import get_api_key

def account(browser: bool = False) -> dict:
    """
    Retrieve account usage and quota. If browser=True, opens the account page.
    """
    if browser:
        webbrowser.open("https://quantkiosk.com/account")
        return {}

    api_key = get_api_key()
    url = f"https://api.qkiosk.io/account?apiKey={api_key}"
    resp = requests.get(url)
    if resp.status_code != 200:
        raise RuntimeError(
            "permission denied - verify your API key is set"
        )
    return resp.json()

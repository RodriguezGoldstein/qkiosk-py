"""
Universe endpoints for QKiosk Python API.
"""
import requests

from .config import get_api_key

def univ(univ_code: str, src: str = "QK", cache: bool = True) -> list:
    """
    Retrieve a universe definition by code.

    Args:
        univ_code: Identifier for the universe (e.g. 'QK100').
        src: Source namespace, default 'QK'.
        cache: Ignored in Python client; for API compatibility.

    Returns:
        List of QKIDs for the universe.
    """
    api_key = get_api_key()
    if src == "QK":
        url = (
            f"https://api.qkiosk.io/univ/QK/{univ_code}/{univ_code}?apiKey={api_key}"
        )
    else:
        raise NotImplementedError("local universe files not supported yet")
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json().get("qkid", [])

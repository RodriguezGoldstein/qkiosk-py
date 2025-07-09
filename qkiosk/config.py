"""
Configuration utilities for QKiosk Python API.
"""
import os

def set_api_key(api_key: str) -> None:
    """
    Set the QK_API_KEY environment variable for API access.
    """
    os.environ["QK_API_KEY"] = api_key

def get_api_key(require: bool = True) -> str:
    """
    Get the QK_API_KEY from environment. Raises if required and not set.
    """
    key = os.getenv("QK_API_KEY")
    if require and not key:
        raise RuntimeError(
            "apiKey not found in QK_API_KEY environment variable."
        )
    return key or ""

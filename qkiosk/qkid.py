"""
QKID conversion utilities for QKiosk Python API.
"""

import re

_QKID_REGEX = re.compile(
    r"([0-9]{10})[.]([A-Z0-9]{4})[.]([BCDFGHJKLMNPQRSTVWXYZ0-9]{9})|"
    r"([0-9]{10})[.]([A-Z0-9]{4})[.](UF[CDFGHJKLMNPQRSTVWXYZ0-9]{6}[A])"
)

def to_qkid(value: str) -> str:
    """
    Validate and return the QKID string if it matches expected pattern.
    """
    qkid = str(value)
    if _QKID_REGEX.fullmatch(qkid):
        return qkid
    raise ValueError(f"Invalid QKID format: {qkid}")

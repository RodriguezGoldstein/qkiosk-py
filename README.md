# QKiosk Python Client

Official Python interface to the QUANTkiosk data API.

![QK Logo](https://quantkiosk.com/assets/img/qk-logo.png)

> **FREE API keys are now enabled for all accounts.** Get yours at https://quantkiosk.com/account

## Features

* Pythonic DataFrame interface via **pandas**
* Minimal dependencies (`requests`, `pandas`)
* Full coverage of endpoints: Account, Universe, Ownership, Fundamentals, Filings, Audit
* Symbology utilities for QKID search and conversion
* Stylers for interactive highlights

## Installation

Install from PyPI:
```bash
pip install qkiosk
```

Or install the development version:
```bash
git clone https://github.com/quantkiosk/qkiosk-py.git
cd qkiosk-py
pip install -e .
```

## Setup your API key

All access to live and historical data requires a valid `QK_API_KEY` environment variable.  For example:

```bash
export QK_API_KEY=""
```

Or at runtime:
```python
from qkiosk.config import set_api_key
# set the API key in-process (same key):
set_api_key("")
```

## Get Started

### Symbology drives everything

Convert tickers or CIKs to QKIDs:
```python

from qkiosk.qkid import to_qkid, qk_ticker

# To validate or parse a full QKID:
valid_qkid = to_qkid("0000320193.0000.001S5N8V8")
# To lookup by ticker (equivalent to R's qk_ticker):
try:
    apple_qkid = qk_ticker("AAPL")
    print("AAPL →", apple_qkid)
except Exception as e:
    print("Error retrieving QKID for AAPL:", e)
```

### Account

```python
from qkiosk.account import account
info = account()
print(info)
```

### Universe

```python
from qkiosk.univ import univ
u = univ("QK100")
print(u)
```

### Fundamentals

```python
from qkiosk.fundamentals import fundamentals

df = fundamentals([
    "0000320193.0000.001S5N8V8"
], items=["SALE","EBIT"], as_json=False)
print(df.head())
```

### Ownership

```python
from qkiosk.ownership import beneficial, insider, holders, institutional

# Beneficial (13D/13G)
b = beneficial("0000320193.0000.001S5N8V8", 202301)
print(b.head())

# Insider (345)
i = insider("0000320193.0000.001S5N8V8", 202301)
print(i.head())
```

### Filings

```python
from qkiosk.complete import complete

# Download and extract filings
res = complete("filings_dir", rollup="10m")
print(res)
```

### Audit

```python
from qkiosk.audit import audit

# Assuming df is a DataFrame from fundamentals or ownership
a = audit(df, row=0)
print(a['url'])
```

For more examples, refer to the docstrings in each module.

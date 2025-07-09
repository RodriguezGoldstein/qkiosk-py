# QKiosk Python Client

This package provides a Pythonic interface to the QUANTkiosk data API, mirroring the functionality available in the R client.

## Installation

```bash
pip install qkiosk
```

## Setup your API key

All access to live and historical data requires a valid `QK_API_KEY`. You can set it in your environment:

```bash
export QK_API_KEY=<YOUR_API_KEY>
```

Or at runtime:
```python
from qkiosk.config import set_api_key
set_api_key("<YOUR_API_KEY>")
```

## Usage

Basic account information:
```python
from qkiosk.account import account
info = account()
```

Retrieve a universe definition:
```python
from qkiosk.univ import univ
u = univ("QK100")
```

For full documentation and examples, see the docstrings in each module.

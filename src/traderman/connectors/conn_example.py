
# --- 

import os
import time
import json
import base64
import hmac
import hashlib
from urllib.parse import urlencode
import binance as binanceSpot

import requests
import numpy as np
import pandas as pd

binance_api_key = os.environ["BINANCE_API_KEY"]
binance_secret_key = os.environ["BINANCE_SECRET_KEY"]

# --- -------------------------------------------------- GET ACCOUNT INFO --- #
# --- -------------------------------------------------- ---------------- --- #

"""
params = {}
response = binanceSpot.account_info(api_key=binance_api_key,
                                    secret_key=binance_secret_key)
print(response)
"""

# --- ------------------------------------------------- GET PUBLIC TRADES --- #
# --- ------------------------------------------------- ----------------- --- #

"""
params = {"symbol": "BTCUSDT"}
response = binanceSpot.public_trades(in_params=params,
                                     api_key=binance_api_key)

print(response)
"""

# --- ---------------------------------------------------- POST NEW ORDER --- #
# --- ---------------------------------------------------- -------------- --- #

"""
params = {"symbol": "BTCUSDT",
          "side": "BUY",
          "type": "LIMIT",
          "price": "61000",
          "timeInForce": "GTC",
          "quantity": "0.0001",
          }

response = binanceSpot.new_order(in_params=params,
                                 api_key=binance_api_key,
                                 secret_key=binance_secret_key,)
print(response)
"""

# --- ---------------------------------------------------- GET ALL ORDERS --- #
# --- ---------------------------------------------------- -------------- --- #

"""
params = {"symbol": "BTCUSDT"}
response = binanceSpot.get_all_orders(in_params=params,
                                   api_key=binance_api_key,
                                   secret_key=binance_secret_key,)
print(len(response))
print(response[0].keys())
"""

# --- --------------------------------------------------- GET ORDERS INFO --- #
# --- --------------------------------------------------- --------------- --- #

"""
params = {"symbol": "BTCUSDT", "orderId": 28009727037}
response = binanceSpot.query_order(in_params=params,
                                   api_key=binance_api_key,
                                   secret_key=binance_secret_key,
                                   )
print(response)
"""

# --- ----------------------------------------------------- CANCEL ORDERS --- #
# --- ----------------------------------------------------- ------------- --- #

"""
params = {"symbol": "BTCUSDT", "orderId": 1234}
response = binanceSpot.cancel_order(in_params=params,
                                    api_key=binance_api_key,
                                    secret_key=binance_secret_key,
                                    )
print(response)
"""


# --- ------------------------------------------------- CANCEL ALL ORDERS --- #
# --- ------------------------------------------------- ----------------- --- #

"""
params = {"symbol": "BTCUSDT"}
response = binanceSpot.cancel_all_orders(in_params=params,
                                         api_key=binance_api_key,
                                         secret_key=binance_secret_key,
                                         )
print(response)
"""


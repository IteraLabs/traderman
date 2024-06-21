
# --- 
import os
import time
import json
import base64
import hmac
import hashlib
from urllib.parse import urlencode

import requests
import numpy as np
import pandas as pd
from tools.data import load_csv
from target.directional import target_y, eda_y
from connectors.binance import send_signed_request, send_public_request

# env_binance_api_key = os.environ["BINANCE_API_KEY"]
# env_binance_secret_key = os.environ["BINANCE_SECRET_KEY"]

# Input file
file_name = "AVAXUSDC-1h-2024-05.csv"
file_route = "~/git/iteralabs/Traderman/files/datasets/"
data = load_csv(file_name, file_route)

# Thresholds for target class definition
y_th = [np.float64("inf")*-1, -2000, -100, 100, 2000, np.float64("inf")]

# Target generation
data["y_t"] = target_y(y_thresholds=y_th, df_data=data)
data["co_t"] = (data["close"] - data["open"])*1e4

# Lightweighted dataset for explorations
data_model = data[["opentime", 'co_t', "y_t"]]
# print(data_model.head(5))
# print(data_model.tail(5))
# data_eda = eda_y(target_y=data_model["y_t"], y_type="categorical")

# -- Open Market or Limit order 
params = {
    "symbol": "BTCUSDT",
    "side": "BUY",
    "type": "MARKET",
    "quoteOrderQty": "10",
}

# response = send_signed_request("POST", "/api/v3/order", params)
# print(response)


# -- Get historical orders
params = {
    "symbol": "BTCUSDT",
}

# response = send_signed_request("GET", "/api/v3/allOrders", params)
# print(response)

# -- Get account information
params = {}

response = send_signed_request("GET", "/api/v3/account", params)
print(response)


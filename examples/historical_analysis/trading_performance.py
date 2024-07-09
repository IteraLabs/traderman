# --- ----------------------------------------------------------------------- #
# --- File: examples/historical_analysis/trading_performance.py
# --- ----------------------------------------------------------------------- #

import os
from traderman.connectors import binance as BinanceSpot

BINANCE_API_KEY = os.environ["BINANCE_API_KEY"]
BINANCE_SECRET_KEY = os.environ["BINANCE_SECRET_KEY"]

acc_data = BinanceSpot.account_trades(
    in_params={"symbol": "BTCUSDT"},
    api_key=BINANCE_API_KEY,
    secret_key=BINANCE_SECRET_KEY,
    format_output=True,
)

print(f"Amount of trades: {len(acc_data)}")
print(f"One trade info is: \n\n{acc_data[0]}")

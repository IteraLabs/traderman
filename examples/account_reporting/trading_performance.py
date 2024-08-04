# --- ----------------------------------------------------------------------- #
# --- File: examples/account_reporting/trading_performance.py
# --- ----------------------------------------------------------------------- #

import os
from traderman.connectors import binance as BinanceSpot
from traderman.generators.dataReport import generate_report as Reporter

BINANCE_API_KEY = os.environ["BINANCE_API_KEY"]
BINANCE_SECRET_KEY = os.environ["BINANCE_SECRET_KEY"]

binance_keys = {
    "BINANCE_API_KEY": os.environ["BINANCE_API_KEY"],
    "BINANCE_SECRET_KEY": os.environ["BINANCE_SECRET_KEY"],
}

report_trades, report_account = Reporter(
    account_client=BinanceSpot, account_keys=binance_keys
)

print(report_trades)
print(report_account)

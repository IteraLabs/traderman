# --- ------------------------------------------------------------------- --- #
# --- File: generators/dataReport.py
# --- ------------------------------------------------------------------- --- #

import attrs
from datetime import datetime as dt
import pandas as pd

# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


def trade_to_report(account_trades: list):
    """
    A format-parser of private trades into report-friendly format
    """

    l_df_trade = []
    dt_str = "%Y-%m-%dT%H:%M:%S.%f"

    for i_trade in account_trades:

        i_trade = attrs.asdict(i_trade)
        ts_us = i_trade["timestamp"] / 1e3
        i_trade["timestamp"] = dt.fromtimestamp(ts_us).strftime(dt_str)

        l_df_trade.append(pd.DataFrame(pd.json_normalize(i_trade)))

    return pd.concat(l_df_trade, axis=0)


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


def generate_report(account_client, account_keys: dict):
    """ """

    acc_info = account_client.account_info(
        in_params={"omitZeroBalances": "true"},
        api_key=account_keys["BINANCE_API_KEY"],
        secret_key=account_keys["BINANCE_SECRET_KEY"],
    )

    acc_trades = account_client.account_trades(
        in_params={"symbol": "BTCUSDT"},
        api_key=account_keys["BINANCE_API_KEY"],
        secret_key=account_keys["BINANCE_SECRET_KEY"],
        format_output=True,
    )

    data_trades_report = trade_to_report(account_trades=acc_trades)
    data_account_report = acc_info

    return data_trades_report, data_account_report

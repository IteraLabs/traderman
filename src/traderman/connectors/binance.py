# --- ------------------------------------------------------------------- --- #
# --- File: binance.py
# --- ------------------------------------------------------------------- --- #

import os
import pandas as pd
import traderman.connectors.clients as ct

BASE_URL = "https://api.binance.com"
HASH_METHOD = "sha256"

# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
def test_connection():

    sr = ct.send_public_request("/api/v1/ping", {}, BASE_URL, None)

    return sr


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
def account_info(api_key, secret_key):
    """
    Get the account information
    """

    sr = ct.send_signed_request(
        "GET",
        "/api/v3/account",
        {},
        BASE_URL,
        api_key,
        secret_key,
    )

    return sr


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
def account_trades(api_key, secret_key):
    """
    Get the account's historical trades
    """

    sr = ct.send_signed_request(
        "GET",
        "/api/v3/myTrades",
        {},
        BASE_URL,
        api_key,
        secret_key,
    )

    return sr


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
def account_comission(in_params, api_key, secret_key):
    """
    Get the account's comission rates
    """

    sr = ct.send_signed_request(
        "GET",
        "/api/v3/account/commission",
        in_params,
        BASE_URL,
        api_key,
        secret_key,
    )

    return sr


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
def new_order_test(in_params, api_key, secret_key):
    """
    place a new TEST order, not real volume, only to validate request

    Args:

        in_params: dict (default={})
        "symbol": "BTCUSDT"
        "side": "SELL"
        "type": "MARKET"

    """

    sr = ct.send_signed_request(
        "POST",
        "/api/v3/order/test",
        in_params,
        BASE_URL,
        api_key,
        secret_key,
    )

    return sr


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
def new_order(in_params, api_key, secret_key):
    """
    place a new order

    Args:

        in_params: dict (default={})
        "symbol": "BTCUSDT"
        "side": "SELL"
        "type": "MARKET"

    """

    sr = ct.send_signed_request(
        "POST",
        "/api/v3/order",
        in_params,
        BASE_URL,
        api_key,
        secret_key,
    )

    return sr


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
def query_order(in_params, api_key, secret_key):
    """
    get the available info for a given order
    """

    sr = ct.send_signed_request(
        "GET",
        "/api/v3/order",
        in_params,
        BASE_URL,
        api_key,
        secret_key,
    )

    return sr


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
def cancel_order(in_params, api_key, secret_key):
    """
    cancel a given order
    """

    sr = ct.send_signed_request(
        "DELETE",
        "/api/v3/order",
        in_params,
        BASE_URL,
        api_key,
        secret_key,
    )

    return sr


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
def cancel_all_orders(in_params, api_key, secret_key):
    """
    cancel all open orders for a particular symbol
    """

    sr = ct.send_signed_request(
        "DELETE",
        "/api/v3/openOrders",
        in_params,
        BASE_URL,
        api_key,
        secret_key,
    )

    return sr


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
def get_all_orders(in_params, api_key, secret_key):
    """
    get all orders (open, filled, cancelled) for a given instrument in a
    given period of time
    """

    sr = ct.send_signed_request(
        "GET",
        "/api/v3/allOrders",
        in_params,
        BASE_URL,
        api_key,
        secret_key,
    )

    return sr


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
def public_trades(in_params, api_key):
    """
    get all public trades for a given symbol
    """

    sr = ct.send_signed_request(
        "GET",
        "/api/v3/trades",
        in_params,
        BASE_URL,
        api_key,
    )

    return sr

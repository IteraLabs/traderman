# --- ------------------------------------------------------------------- --- #
# --- File: test_binance_api_spot.py
# --- ------------------------------------------------------------------- --- #

import sys
import os
import time
import json
import unittest

import requests
import numpy as np
import pandas as pd


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


def load_env(verbose: bool = False):

    local_abs_path = os.path.abspath(".")
    print("Loading environment") if verbose else None
    print(f"The local abs path is: {local_abs_path}") if verbose else None
    traderman_path = local_abs_path + "/src/"
    print(f"inserting this into path: {traderman_path}") if verbose else None
    sys.path.insert(0, traderman_path)


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


class BinanceKeys(unittest.TestCase):
    """
    Test the presence of Binance REST API keys in the environment
    """

    def test_binance_api_key(self):

        self.assertIsNotNone(os.environ["BINANCE_API_KEY"])

    def test_binance_secret_key(self):

        self.assertIsNotNone(os.environ["BINANCE_SECRET_KEY"])


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


class BinanceGeneral(unittest.TestCase):
    """ """

    def test_connection(self):
        """
        Test the connection to Binance REST API server as  specified
        in the url
        """

        response = binanceSpot.test_connection()

        self.assertIsNotNone(response)


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


class BinanceAccount(unittest.TestCase):
    """
    Test the Account Endpoints for the Binance REST API

    References:
        api_url: "https://developers.binance.com/"
        docs_url: "docs/binance-spot-api-docs/rest-api"
    """

    # --- --------------------------------------------------------------- --- #
    # --- --------------------------------------------------------------- --- #
    def test_account_info(self):
        """
        Test the #account-information-user_data endpoint
        """

        params = {}

        response = binanceSpot.account_info(
            api_key=BINANCE_API_KEY, secret_key=BINANCE_SECRET_KEY
        )

        self.assertIsNotNone(response)

    # --- --------------------------------------------------------------- --- #
    # --- --------------------------------------------------------------- --- #
    def test_account_trades(self, test_symbol: str = "BTCUSDT"):
        """
        Test the #account-trade-list-user_data endpoint
        """

        params = {}

        response = binanceSpot.account_trades(
            api_key=BINANCE_API_KEY, secret_key=BINANCE_SECRET_KEY
        )

        self.assertIsNotNone(response)

    # --- --------------------------------------------------------------- --- #
    # --- --------------------------------------------------------------- --- #
    def test_account_comission(self, test_symbol: str = "BTCUSDT"):
        """
        Test the #query-commission-rates-user_data endpoint
        """

        params = {"symbol": "BTCUSDT"}

        response = binanceSpot.account_comission(
            in_params=params,
            api_key=BINANCE_API_KEY,
            secret_key=BINANCE_SECRET_KEY,
        )

        self.assertIsNotNone(response)


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


class BinanceMarketData(unittest.TestCase):
    """ """

    # --- --------------------------------------------- GET PUBLIC TRADES --- #
    # --- --------------------------------------------- ----------------- --- #

    def test_public_trades(self):
        """
        Test the #recent-trades-list endpoint
        """

        params = {"symbol": "BTCUSDT"}

        response = binanceSpot.public_trades(
            in_params=params,
            api_key=BINANCE_API_KEY,
        )

        self.assertIsNotNone(response)


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


class BinanceTrading(unittest.TestCase):
    """
    Test private trading endpoints
    """

    # --- ------------------------------------------- POST NEW TEST ORDER --- #
    # --- ------------------------------------------- ------------------- --- #
    def test_new_order_test(self):
        """
        Test posting a TEST new order, not real volume
        """

        params = {
            "symbol": "BTCUSDT",
            "side": "BUY",
            "type": "LIMIT",
            "price": "61000",
            "timeInForce": "GTC",
            "quantity": "0.0001",
        }

        response = binanceSpot.new_order_test(
            in_params=params,
            api_key=BINANCE_API_KEY,
            secret_key=BINANCE_SECRET_KEY,
        )

        self.assertIsNotNone(response)

    # --- ------------------------------------------------ GET ALL ORDERS --- #
    # --- ------------------------------------------------ -------------- --- #

    def test_get_all_orders(self):
        """
        Test #all-orders-user_data endpoint
        """

        params = {"symbol": "BTCUSDT"}
        response = binanceSpot.get_all_orders(
            in_params=params,
            api_key=BINANCE_API_KEY,
            secret_key=BINANCE_SECRET_KEY,
        )

        self.assertIsNotNone(response)


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


if __name__ == "__main__":

    load_env(verbose=True)

    from traderman.connectors import binance as binanceSpot

    BINANCE_API_KEY = os.environ["BINANCE_API_KEY"]
    BINANCE_SECRET_KEY = os.environ["BINANCE_SECRET_KEY"]

    unittest.main()

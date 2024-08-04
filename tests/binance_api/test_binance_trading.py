# --- ------------------------------------------------------------------- --- #
# --- File: test_binance_account.py
# --- ------------------------------------------------------------------- --- #

import os
import unittest
from traderman.connectors import binance as binanceSpot


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


class BinanceTrading(unittest.TestCase):
    """
    Test the Trading Endpoints for the Binance REST API

    References:
        api_url: "https://developers.binance.com/"
        docs_url: "docs/binance-spot-api-docs/rest-api"
    """

    # --- --------------------------------------------------------------- --- #
    # --- --------------------------------------------------------------- --- #
    def test_new_order_test(self):
        """
        Test the #new-order-test
        """

        response = binanceSpot.new_order_test(
            in_params={},
            api_key=BINANCE_API_KEY,
            secret_key=BINANCE_SECRET_KEY,
        )

        self.assertIsNotNone(response)

    # --- --------------------------------------------------------------- --- #
    # --- --------------------------------------------------------------- --- #
    def test_new_order(self):
        """
        Test the #new-order-test
        """

        params = {"symbol": "BTCUSDT", "side": "SELL", "type": "MARKET"}

        response = binanceSpot.new_order(
            in_params=params,
            api_key=BINANCE_API_KEY,
            secret_key=BINANCE_SECRET_KEY,
        )

        self.assertIsNotNone(response)

    # --- --------------------------------------------------------------- --- #
    # --- --------------------------------------------------------------- --- #
    def test_all_orders(self):
        """
        Test the #new-order-test
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

    from traderman.connectors import binance as binanceSpot

    BINANCE_API_KEY = os.environ["BINANCE_API_KEY"]
    BINANCE_SECRET_KEY = os.environ["BINANCE_SECRET_KEY"]

    unittest.main()

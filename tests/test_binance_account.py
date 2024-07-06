# --- ------------------------------------------------------------------- --- #
# --- File: test_binance_account.py
# --- ------------------------------------------------------------------- --- #

import sys
import os
import unittest

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

        response = binanceSpot.account_info(
            api_key=BINANCE_API_KEY, secret_key=BINANCE_SECRET_KEY
        )

        self.assertIsNotNone(response)

    # --- --------------------------------------------------------------- --- #
    # --- --------------------------------------------------------------- --- #
    def test_account_trades(self):
        """
        Test the #account-trade-list-user_data endpoint
        """

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

        params = {"symbol": test_symbol}

        response = binanceSpot.account_comission(
            in_params=params,
            api_key=BINANCE_API_KEY,
            secret_key=BINANCE_SECRET_KEY,
        )

        self.assertIsNotNone(response)


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


if __name__ == "__main__":

    import sys
    import os

    local_abs_path = os.path.abspath(".")
    print("Loading environment")
    print(f"The local abs path is: {local_abs_path}")
    traderman_path = local_abs_path + "/src/"
    print(f"inserting this into path: {traderman_path}")
    sys.path.insert(0, traderman_path)

    from traderman.connectors import binance as binanceSpot

    BINANCE_API_KEY = os.environ["BINANCE_API_KEY"]
    BINANCE_SECRET_KEY = os.environ["BINANCE_SECRET_KEY"]

    unittest.main()

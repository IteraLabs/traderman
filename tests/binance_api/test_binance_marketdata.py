# --- ------------------------------------------------------------------- --- #
# --- File: test_binance_public.py
# --- ------------------------------------------------------------------- --- #

import sys
import os
import unittest

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

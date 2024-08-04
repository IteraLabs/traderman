# --- ------------------------------------------------------------------- --- #
# --- File: test_marketdata_t.py
# --- ------------------------------------------------------------------- --- #

import sys
import os
import unittest

# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


class MarketDataT(unittest.TestCase):
    """
    Container class for Trade data
    """

    # --- ----------------------------------------- TEST A TRADE INSTANCE --- #
    # --- --------------------------------------------------------------- --- #

    def test_trade(self):
        """
        Test the correctness of the Trade Structure type
        """

        i_trade = Trade(
            tradeid=123,
            orderid=123,
            symbol="btcusdt",
            timestamp=1267918039,
            price=60123.1234,
            side="BUY",
            volume={"base": 312.123, "quote": 123.321},
            commission={"amount": 123.321, "asset": "BTC"},
        )

        self.assertIsNotNone(i_trade)


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

    from traderman.core.marketdataTypes import Trade

    unittest.main()

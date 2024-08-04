# --- ------------------------------------------------------------------- --- #
# --- File: test_marketdata_o.py
# --- ------------------------------------------------------------------- --- #

import sys
import os
import unittest

# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


class MarketDataO(unittest.TestCase):
    """
    Container class for Order data
    """

    # --- ----------------------------------------- TEST A TRADE INSTANCE --- #
    # --- --------------------------------------------------------------- --- #

    def test_order(self):
        """
        Test the correctness of the Order Structure type
        """

        i_order = Order(
            orderid=123,
            symbol="btcusdt",
            timestamp=1267918039,
            price=60123.1234,
            side="BUY",
            volume=123.4321,
            ordertype="MARKET",
        )

        self.assertIsNotNone(i_order)


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

    from traderman.core.marketdataTypes import Order

    unittest.main()

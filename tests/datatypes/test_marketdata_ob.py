# --- ------------------------------------------------------------------- --- #
# --- File: test_marketdata_ob.py
# --- ------------------------------------------------------------------- --- #

import sys
import os
import unittest

# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


class MarketDataOB(unittest.TestCase):
    """ """

    # --- ------------------------------------ TEST AN ORDERBOOK INSTANCE --- #
    # --- --------------------------------------------------------------- --- #

    def test_orderbook(self):
        """
        Test the correctness of the OrderBook Structure type
        """

        i_bids = Bids(
            prices=torch.tensor([0.1, 0.05]), volumes=torch.tensor([1.1, 1.5])
        )

        i_asks = Asks(
            prices=torch.tensor([0.2, 0.25]), volumes=torch.tensor([2.1, 0.5])
        )

        i_orderbook = OrderBook(
            orderbookid=123,
            symbol="btcusdt",
            timestamp=1267918039,
            bids=i_bids,
            asks=i_asks,
        )

        self.assertIsNotNone(i_orderbook)


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

    import torch
    from traderman.core.marketdataTypes import OrderBook, Bids, Asks

    unittest.main()

# --- ------------------------------------------------------------------- --- #
# --- File: test_binance_connection.py
# --- ------------------------------------------------------------------- --- #

import sys
import os
import unittest

# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


class BinanceConnection(unittest.TestCase):
    """ """

    # --- --------------------------------------------- TEST A CONNECTION --- #
    # --- --------------------------------------------- ----------------- --- #

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

    unittest.main()

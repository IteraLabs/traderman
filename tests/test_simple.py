# --- ------------------------------------------------------------------- --- #
# --- File: test_simple.py
# --- ------------------------------------------------------------------- --- #

import os
import unittest

#  --- ------------------------------------------------------------------ --- #
#  --- ------------------------------------------------------------------ --- #
#  --- ------------------------------------------------------------------ --- #


class TestSimple(unittest.TestCase):
    def test_binance_api_key(self):

        self.assertIsNotNone(os.environ["BINANCE_API_KEY"])

    def test_binance_secret_key(self):

        self.assertIsNotNone(os.environ["BINANCE_SECRET_KEY"])


if __name__ == "__main__":
    unittest.main()

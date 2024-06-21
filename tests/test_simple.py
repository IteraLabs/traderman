
# ---

import os
import unittest
from traderman.dataloader import load_csv
test_file = os.getcwd(".")

class TestSimple(unittest.TestCase):

    def test_load_data(self):

        self.assertIsNotNone(load_csv(""))

if __name__ == '__main__':
    unittest.main()



import os
import sys
real_path = os.path.realpath("./src")
sys.path.insert(0, real_path + "/traderman")
print(real_path)
print(sys.path)

import src.traderman as traderman 
__all__ = ["traderman"]


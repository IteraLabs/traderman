
# --- -------------------------------------------------------------------- -- #
# --- -------------------------------------------------------------------- -- #

import os
import sys
import toml

# -- Set working directories
cwd_path = os.getcwd()
package_path = cwd_path + "/src"
sys.path.insert(0, package_path)

from traderman.forecasters.benchmarks import Randomizer
from traderman.connectors import binance as BinanceSpot

# --- Get params from Config.toml 

with open(cwd_path + "/examples/basic_config.toml", "r") as file:
    config_data = toml.load(file)

SET_SEED = config_data["model"]["signal"]["model_params"]["seed"]
SET_CLASSES = config_data["model"]["signal"]["model_params"]["classes"]

# -- 

ModelSignal = Randomizer(seed=SET_SEED)
forecasted_signal = ModelSignal.predict(predict_type="class",
                                        classes=SET_CLASSES)

#ModelRisk = 1

print(f"forecasted class: {forecasted_signal}")
#print(f"volume to trade: {trade_volume}")

# -- Trade Layer

#BinanceSpot.new_order()


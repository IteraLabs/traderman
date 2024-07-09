# --- ------------------------------------------------------------------- --- #
# --- File: basic_trading.py -------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #

import os
import toml
import numpy as np

from traderman.forecasters.benchmarks import Randomizer
from traderman.connectors import binance as BinanceSpot

BINANCE_API_KEY = os.environ["BINANCE_API_KEY"]
BINANCE_SECRET_KEY = os.environ["BINANCE_SECRET_KEY"]

# --- Get params from Config.toml --------------------------------------- --- #

cwd_path = os.path.abspath("")
with open(cwd_path + "/examples/basic_config.toml", "r") as file:
    config_data = toml.load(file)

SET_SEED = config_data["model"]["signal"]["model_params"]["seed"]
SET_CLASSES = config_data["model"]["signal"]["model_params"]["classes"]

# --- ------------------------------------------------------------------- --- #

ModelSignal = Randomizer(seed=SET_SEED, model_type="classifier")
forecasted_signal = ModelSignal.predict(classes=SET_CLASSES)

print(f"forecasted class: {forecasted_signal}")

# --- ------------------------------------------------------------------- --- #

ModelRisk = Randomizer(seed=SET_SEED, model_type="regressor")
forecasted_volume = ModelRisk.predict(lower=0.0001, upper=0.0002)
forecasted_volume = np.round(np.float32(forecasted_volume), 4)

print(f"volume to trade: {forecasted_volume}")

# --- ------------------------------------------------------------------- --- #
trade_params = {
    "symbol": "BTCUSDT",
    "type": "MARKET",
    "side": forecasted_signal,
    "quantity": forecasted_volume[0],
}

n_order = BinanceSpot.new_order(
    in_params=trade_params, api_key=BINANCE_API_KEY, secret_key=BINANCE_SECRET_KEY
)

print(n_order)

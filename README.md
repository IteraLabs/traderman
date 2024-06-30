# Traderman
Python SDK to build, train, stress-test, deploy and monitor trading strategies

[![stars](https://img.shields.io/github/stars/iteralabs/traderman)](https://github.com/iteralabs/traderman/stargazers)
[![issues](https://img.shields.io/github/issues/iteralabs/traderman)](https://github.com/iteralabs/traderman/issues)
[![forks](https://img.shields.io/github/forks/iteralabs/traderman)](https://github.com/iteralabs/traderman/network/members)
[![version](https://badge.fury.io/py/traderman.svg)](https://pypi.org/project/traderman)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/iteralabs/tradernab/blob/master/.pre-commit-config.yaml)
[![License](https://img.shields.io/github/license/iteralabs/traderman)](https://github.com/iteralabs/traderman/blob/master/LICENSE)
[![python](https://img.shields.io/badge/-Python_3.11-blue?logo=python&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pytorch](https://img.shields.io/badge/PyTorch_2.0+-ee4c2c?logo=pytorch&logoColor=white)](https://pytorch.org/get-started/locally/)

<br>


## Install

Using `pip`

```
pip install traderman
```

Cloning the repository

```
git clone https://github.com/iteralabs/traderman.git
```

<br>

## Use

```python

import os
import toml
import numpy as np

from traderman.forecasters.benchmarks import Randomizer
from traderman.connectors import binance as BinanceSpot

BINANCE_API_KEY = os.environ["BINANCE_API_KEY"]
BINANCE_SECRET_KEY = os.environ["BINANCE_SECRET_KEY"]

# --- Get params from Config.toml

with open(cwd_path + "/examples/basic_config.toml", "r") as file:
    config_data = toml.load(file)

SET_SEED = config_data["model"]["signal"]["model_params"]["seed"]
SET_CLASSES = config_data["model"]["signal"]["model_params"]["classes"]

# --- Use the randomizer as model benchmark

ModelSignal = Randomizer(seed=SET_SEED, model_type="classifier")
forecasted_signal = ModelSignal.predict(classes=SET_CLASSES)

ModelRisk = Randomizer(seed=SET_SEED, model_type="regressor")
forecasted_volume = np.round(ModelRisk.predict(lower=0.0001, upper=0.0009), 4)

# --- Specify parameters for trades

trade_params = {
    "symbol": "BTCUSDT",
    "type": "MARKET",
    "side": forecasted_signal,
    "quantity": forecasted_volume[0],
}

# --- Place an Order

n_order = BinanceSpot.new_order(
    in_params=trade_params,
    api_key=BINANCE_API_KEY,
    secret_key=BINANCE_SECRET_KEY
)

```

<br>

## 📃 Contributors

Everyone can contribute and make a difference. Thanks to:  

<a href="https://github.com/iteralabs/traderman/graphs/contributors">
  <img class="dark-light" src="https://contrib.rocks/image?repo=iteralabs/traderman&anon=0&columns=20&max=100&r=true" />
</a>
 
Check out the following ways to contribute:

- Check the [Open Tasks](https://ivy.dev/docs/overview/contributing/open_tasks.html) and the [Contributing guide](https://ivy.dev/docs/overview/contributing.html)

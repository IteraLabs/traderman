# --- ------------------------------------------------------------------- --- #
# --- File: data.py
# --- ------------------------------------------------------------------- --- #

import pandas as pd

# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


def load_csv(file_name, file_route, **args):
    """ """

    data = pd.read_csv(file_route + file_name, header=None)
    data.columns = [
        "opentime",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "closetime",
        "quote_asset_volume",
        "number_of_trades",
        "taker_buy_base_asset_volume",
        "taker_buy_quote_asset_volume",
        "ignore",
    ]

    # Convert to ISO 8601 timestamps
    data["opentime"] = [
        pd.to_datetime(data["opentime"][i] * 1e6) for i in range(0, len(data))
    ]
    data["closetime"] = [
        pd.to_datetime(data["closetime"][i] * 1e6) for i in range(0, len(data))
    ]

    data.drop("ignore", axis=1, inplace=True)

    return data

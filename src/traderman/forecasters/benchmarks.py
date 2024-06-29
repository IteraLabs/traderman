# --- ----------------------------------------------------------------------- #
# --- File: benchmarks.py
# --- ----------------------------------------------------------------------- #

import sys
import os
import torch
from torch.distributions.uniform import Uniform
from traderman.forecasters.forecast import Forecaster

# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


class Randomizer(Forecaster):
    """ """

    # ----------------------------------------------------------------------- #
    # ----------------------------------------------------------------------- #

    def __init__(self, seed: int, model_type: str) -> None:
        """ """

        self.seed = seed
        self.model_type = model_type

    # ----------------------------------------------------------------------- #
    # ----------------------------------------------------------------------- #

    def predict(self, verbose: bool = False, **kwargs):
        """ """

        if self.model_type == "classifier":

            i_index = torch.randint(len(kwargs["classes"]), (1,))
            forecasted = kwargs["classes"][i_index]

            print(f" -- Forecast: {forecasted}") if verbose else None

            return forecasted

        elif self.model_type == "regressor":

            i_index = Uniform(kwargs["lower"], kwargs["upper"])
            forecasted = i_index.sample([1])

            return forecasted.tolist()[0:]

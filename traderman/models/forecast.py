# --- ----------------------------------------------------------------------- #
# --- File: forecast.py
# --- ----------------------------------------------------------------------- #

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict

# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


class Forecaster(ABC):
    """
    Abstract Factory template class
    """

    @abstractmethod
    def predict(self) -> Dict[str, Any]:
        return {"forecast": 1}

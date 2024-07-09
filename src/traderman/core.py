# --- ----------------------------------------------------------------------- #
# --- File: core.py
# --- ----------------------------------------------------------------------- #

from attrs import validators
from attrs import define, field

# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


@define
class Trade:
    """
    Container class for an already executed trade.

    """

    tradeid: int = field(kw_only=True, validator=validators.instance_of(int))

    orderid: int = field(
        kw_only=True, default=None, validator=validators.instance_of(int)
    )

    symbol: str = field(kw_only=True, validator=validators.instance_of(str))

    timestamp: int = field(kw_only=True, validator=validators.instance_of(int))

    price: float = field(kw_only=True, validator=validators.instance_of(float))

    side: str = field(kw_only=True, validator=validators.in_(["SELL", "BUY"]))

    volume: dict = field(
        kw_only=True,
        validator=validators.deep_mapping(
            key_validator=validators.instance_of(str),
            value_validator=validators.instance_of(float),
            mapping_validator=validators.instance_of(dict),
        ),
    )

    commission: dict = field(kw_only=True)


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


@define
class Order:
    """ """

    orderid: int = field(kw_only=True, validator=validators.instance_of(int))

    timestamp: int = field(kw_only=True, validator=validators.instance_of(int))

    type: str = field(kw_only=True, validator=validators.in_(["MARKET", "LIMIT"]))

    price: float = field(kw_only=True, validator=validators.instance_of(float))

    side: str = field(kw_only=True, validator=validators.in_(["SELL", "BUY"]))

    volume: float = field(kw_only=True, validator=validators.instance_of(float))

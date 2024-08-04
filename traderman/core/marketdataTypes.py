# --- ----------------------------------------------------------------------- #
# --- File: marketdataTypes.py
# --- ----------------------------------------------------------------------- #

import typing
from attrs import validators
from attrs import define, field

from traderman.core.dataTypes import tensorTypes

# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


@define(slots=True, frozen=True)
class Bids:
    prices: typing.Any = field(validator=tensorTypes.validator[0])
    volumes: typing.Any = field(validator=tensorTypes.validator[0])


@define(slots=True, frozen=True)
class Asks:
    prices: typing.Any = field(validator=tensorTypes.validator[0])
    volumes: typing.Any = field(validator=tensorTypes.validator[0])


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


@define(slots=True, frozen=True)
class OrderBook:
    """
    Container class for orderbook data
    """

    orderbookid: int = field(kw_only=True, validator=validators.instance_of(int))

    symbol: str = field(kw_only=True, validator=validators.instance_of(str))

    timestamp: int = field(kw_only=True, validator=validators.instance_of(int))

    bids: Bids = field(kw_only=True, validator=validators.instance_of(Bids))

    asks: Asks = field(kw_only=True, validator=validators.instance_of(Asks))


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


@define(frozen=True)
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
            value_validator=validators.instance_of((float, int)),
            mapping_validator=validators.instance_of(dict),
        ),
    )

    commission: dict = field(
        kw_only=True,
        validator=validators.deep_mapping(
            key_validator=validators.instance_of(str),
            value_validator=validators.instance_of((float, int, str)),
            mapping_validator=validators.instance_of(dict),
        ),
    )


# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #


@define
class Order:
    """ """

    orderid: int = field(kw_only=True, validator=validators.instance_of(int))

    symbol: str = field(kw_only=True, validator=validators.instance_of(str))

    timestamp: int = field(kw_only=True, validator=validators.instance_of(int))

    price: float = field(kw_only=True, validator=validators.instance_of(float))

    side: str = field(kw_only=True, validator=validators.in_(["SELL", "BUY"]))

    volume: float = field(kw_only=True, validator=validators.instance_of(float))

    ordertype: str = field(kw_only=True, validator=validators.in_(["MARKET", "LIMIT"]))

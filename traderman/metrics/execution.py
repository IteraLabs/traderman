# --- ----------------------------------------------------------------------- #
# --- File: metrics/execution.py
# --- ----------------------------------------------------------------------- #

from traderman.core import Trade


def ImplementationShortfall(
    trade: Trade,
):
    """
    An standard benchmark to measure a trading outcome, which is simply the
    execution price compared to the "prevailing" price at the time
    the trader received the order.

    Args:
        trade: dict


        b:

    Returns:
        r:

    Raises:
        raise:

    Complement:
        IS = side * (p_exect - p_arrival) / p_arrival
    """

    is_side = -1 if trade["side"] == "SELL" else 1
    is_price = trade["price"]
    is_parrival = 1

    metric_is = is_side * ((is_price - is_parrival) / is_parrival)

    return metric_is

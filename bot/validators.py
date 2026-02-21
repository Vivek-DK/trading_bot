from typing import Optional

VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT"}


def validate_symbol(symbol: str) -> str:
    if not symbol:
        raise ValueError("Symbol is required")

    symbol = symbol.upper()

    if len(symbol) < 6:
        raise ValueError("Symbol looks invalid (example: BTCUSDT)")

    return symbol


def validate_side(side: str) -> str:
    if not side:
        raise ValueError("Side is required")

    side = side.upper()

    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL")

    return side


def validate_order_type(order_type: str) -> str:
    if not order_type:
        raise ValueError("Order type is required")

    order_type = order_type.upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT")

    return order_type


def validate_quantity(quantity) -> float:
    try:
        quantity = float(quantity)
    except Exception:
        raise ValueError("Quantity must be a number")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    return quantity


def validate_price(order_type: str, price: Optional[float]) -> Optional[float]:
    order_type = order_type.upper()

    if order_type == "LIMIT":
        if price is None or price == "":
            raise ValueError("Price is required for LIMIT orders")

        try:
            price = float(price)
        except Exception:
            raise ValueError("Price must be a number")

        if price <= 0:
            raise ValueError("Price must be greater than 0")

        return price

    return None
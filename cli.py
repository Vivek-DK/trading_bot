import argparse
import sys

from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

from bot.orders import place_market_order, place_limit_order
from bot.logging_config import setup_logger

logger = setup_logger()


def parse_args():
    parser = argparse.ArgumentParser(description="Simple Binance Futures trading bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    return parser.parse_args()


def main():
    args = parse_args()

    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(order_type, args.price)

        if order_type == "MARKET":
            result = place_market_order(symbol, side, quantity)
        else:
            result = place_limit_order(symbol, side, quantity, price)

        print("\nOrder Request")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Qty: {quantity}")
        if price is not None:
            print(f"Price: {price}")

        print("\nResponse")
        for k, v in result.items():
            print(f"{k}: {v}")

        print("\nSuccess")

    except Exception as e:
        logger.error(f"Validation/API failure -> {e}")
        print(f"\n Failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
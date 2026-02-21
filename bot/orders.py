from bot.client import BinanceFuturesClient
from bot.logging_config import setup_logger

logger = setup_logger()


def place_market_order(symbol: str, side: str, quantity: float):
    client = BinanceFuturesClient()

    params = {
        "symbol": symbol,
        "side": side,
        "type": "MARKET",
        "quantity": quantity,
    }

    try:
        logger.info(f"Market order -> {symbol} {side} {quantity}")

        response = client.create_order(**params)

        # summary log (quick glance info)
        logger.info(
            f"Order result -> id={response.get('orderId')} status={response.get('status')}"
        )

        return _format_response(response)

    except Exception as e:
        logger.error(f"Market order failed: {e}")
        raise


def place_limit_order(symbol: str, side: str, quantity: float, price: float):
    client = BinanceFuturesClient()

    params = {
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": quantity,
        "price": price,
    }

    try:
        logger.info(f"Limit order -> {symbol} {side} {quantity} @ {price}")

        response = client.create_order(**params)

        # summary log
        logger.info(
            f"Order result -> id={response.get('orderId')} status={response.get('status')}"
        )

        return _format_response(response)

    except Exception as e:
        logger.error(f"Limit order failed: {e}")
        raise


def _format_response(resp: dict) -> dict:
    return {
        "orderId": resp.get("orderId"),
        "status": resp.get("status"),
        "executedQty": resp.get("executedQty"),
        "avgPrice": resp.get("avgPrice") or resp.get("price"),
        "symbol": resp.get("symbol"),
        "side": resp.get("side"),
        "type": resp.get("type"),
    }
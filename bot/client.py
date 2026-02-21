import os
from binance.client import Client
from dotenv import load_dotenv

from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger()


class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise RuntimeError("Missing Binance API credentials in .env")

        self.client = Client(api_key, api_secret)

        # force futures testnet endpoint
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logger.info("Binance Futures testnet client initialized")

    def create_order(self, **params):
        try:
            logger.debug(f"API REQUEST futures_create_order -> {params}")

            response = self.client.futures_create_order(**params)

            logger.debug(f"API RESPONSE futures_create_order -> {response}")

            return response

        except Exception as e:
            logger.error(f"Order failed: {e}")
            raise
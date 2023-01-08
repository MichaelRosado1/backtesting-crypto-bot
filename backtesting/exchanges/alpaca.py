from typing import *
from secret import API_KEY, SECRET_KEY
from alpaca_trade_api import TimeFrame
import alpaca_trade_api as tradeapi
import logging 

logger = logging.getLogger()
class AlpacaClient:
    def __init__(self):
        self._key_id = API_KEY
        self._secret_key = SECRET_KEY
        self._base_url_ = 'https://paper-api.alpaca.markets'
        self._data_url_ = 'https://data.alpaca.markets'
        self.authenticate_bot()

    def authenticate_bot(self):
        try:
            self._api = tradeapi.REST(
                    self._key_id, 
                    self._secret_key, 
                    self._base_url_
            )
        except Exception as e:            logger.error("Connection error while authenticating bot: %s", e)


    def get_historical_data(self, symbol: str, start_time: Optional[int] = None, end_time: Optional[int] = None):
        raw_candles = self._api.get_crypto_bars(symbol,TimeFrame.Minute,limit=1500, start = '2021-06-08').df
        print(raw_candles)



client = AlpacaClient()
client.get_historical_data("DOGEUSD")


from typing import Optional, Dict, Any, List
from requests import \
    Request, \
    Session, \
    Response, \
    request, \
    exceptions

import hmac
import time



BASE_URL = 'https://app.primebit.com/api/v1'


class PrimebitPublic():

    def __init__(self, type='live'):
        '''live or demo'''
        self.type = type
        self.base_url = BASE_URL

    def _request(self, method: str, api_url: str, params=None):
        '''Public Requests'''
        r_url = self.base_url + api_url
        print(r_url)
        try:
            r = request(method, r_url, params=params)
            print(r)
            r.raise_for_status()
        except exceptions.HTTPError as err:
            print(err)
        if r.status_code == 200:
            return r.json()

    def _get(self, api_url: str, params: Optional[Dict[str, Any]] = None):
        return self._request('GET', api_url, params=params)

    def _assetsDetails(self):
        '''

        :return:
        '''
        return self._get(
            '/trading/assets'
        )

    def assets(self):
        '''
        Details on crypto currencies available on the exchange
        /trading/assets
        :param params:
        :return:
        '''

        return [d for d in self._assetsDetails()]

    def getsymbols(self):
        '''
        Get symbols
        /trading/market_data/symbol/{type}
        :param params:
        :return:
        '''

        return self._get(
            '/trading/market_data/symbol/%s' % (self.type)
        )

    def symbolsDailyStats(self, symbol):
        '''
        Get symbol daily stats
        /trading/market_data/symbol/{type}/{symbol}/daily_stats
        :param params:
        :return:
        '''

        return self._get(
            '/trading/market_data/symbol/%s/%s/daily_stats' % (self.type, symbol)
        )

    def orderBook(self, symbol):
        '''
        Get aggregated 32-levels of order book
        /trading/market_data/order_book/{type}/{symbol}
        :param params:
        :return:
        '''
        return self._get(
            '/trading/market_data/order_book/%s/%s' % (self.type, symbol)
        )

    def getAllTicker(self):
        '''
        Overview of market data for all tickers
        /trading/market_data/summary/{type}
        :param params:
        :return:
        '''
        return self._get(
            '/trading/market_data/summary/%s' % (self.type)
        )

    def getTicker(self, symbol):
        '''
        Get data for a specific ticker
        /trading/market_data/summary/{type}
        :param params:
        :return:
        '''
        tickers = self.getAllTicker()
        return [tickers[Symbol] for Symbol in tickers if Symbol == symbol][0]

    def _tickersStats(self):
        '''
        24-hour rolling window price change statistics for all markets
        /trading/market_data/ticker/{type}
        :param params:
        :return:
        '''
        return self._get(
            '/trading/market_data/ticker/%s' % (self.type)
        )

    def getTickerStat(self, symbol):
        '''
        24-hour rolling window price change statistics for a specific pair
        /trading/market_data/summary/{type}
        :param params:
        :return:
        '''
        ticker = self._tickersStats()
        return [ticker[Symbol] for Symbol in ticker if Symbol == symbol][0]

    def getMarketTrades(self, symbol):
        '''
        Trades completed in the last 24 hours for a given market.
        /trading/market_data/trades/{type}/{symbol}
        :param params:
        :return:
        '''
        return self._get(
            '/trading/market_data/trades/%s/%s' % (self.type, symbol)
        )

    def marketTradeCompleted(self, symbol):
        '''
        Trades completed in the last 10 minutes
        /trading/market_data/trades/{type}/last/{symbol}
        :param params:
        :return:
        '''
        return self._get(
            '/trading/market_data/trades/%s/last/%s' % (self.type, symbol)
        )


class PrimebitPrivate():
    def __init__(self, accountID=None, key=None, secret=None):
        self._session = Session()
        self._account_ID = accountID
        self._api_key = key
        self._api_secret = secret

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None):
        return self._request('GET', path, params=params)

    def _post(self, path: str, params: Optional[Dict[str, Any]] = None):
        return self._request('POST', path, json=params)

    def _delete(self, path: str, params: Optional[Dict[str, Any]] = None):
        return self._request('DELETE', path, json=params)

    def _request(self, method: str, path: str, **kwargs):
        request = Request(method, BASE_URL + path, **kwargs)
        # print('---------------------------------')
        # print(method, BASE_URL + path)

        self._sign_request(request)
        response = self._session.send(request.prepare())
        # print(response)
        return self._process_response(response)

    def _process_response(self, response: Response) -> Any:
        try:
            data = response.json()

        except ValueError:
            response.raise_for_status()
            raise

        return data


    def _sign_request(self, request: Request):
        timestamp = int(time.time())
        prepared = request.prepare()
        '''signature components order matters - should be {method}{body}{path}{query}{timestamp}'''
        signature_payload = f'{prepared.method}{prepared.path_url}{timestamp}'.encode()
        if prepared.body:
            signature_payload += prepared.body
        signature = hmac.new(self._api_secret.encode(), signature_payload, 'sha256').hexdigest()
        request.headers['api-key'] = self._api_key
        request.headers['authorization'] = signature
        request.headers['timestamp'] = str(timestamp)
        # print(request.headers)

    def getAllAccounts(self):
        '''
        GET
        /trading/account
        Get all user accounts

        :param params:
        :return:
        '''
        return self._get(
            '/trading/account'
        )

    def getAccount(self):
        '''
        GET
        /trading/account/{id}
        Get account

        :param params:
        :return:
        '''
        return self._get(
            '/trading/account/%s' % (self._account_ID)
        )

    def getAccountPositions(self):
        '''
        GET
        /trading/account/{account_id}/position
        List account positions

        :param params:
        :return:
        '''
        return self._get(
            '/trading/account/%s/position' % (self._account_ID)
        )

    def getPosition(self, symbol):
        '''
        GET
        /trading/account/{account_id}/position/{symbol}
        Get a particular position

        :param params:
        :return:
        '''
        return self._get(
            '/trading/account/%s/position/%s' % (self._account_ID, symbol),
        )

    def createOrder(self, **params):
        '''
        POST
        Create new order
        /trading/account/{account_id}/order

        :param params:

        Account

        Example Value
        Model
        {
          "volume": "0.01",
          "type": "limit",
          "symbol": "ETHUSDd",
          "stop_price": "0.0",
          "side": "sell",
          "limit_price": "228.7",
          "fill_type": "immediate-or-cancel",
          "comment": "order#32787"
        }

        {
        volume	string
        required: true ***************************
        -------------------------------------------------------------------
        type	string
        market, limit, stop or stop-limit ***************************
        -------------------------------------------------------------------
        symbol	string
        required: true ***************************
        -------------------------------------------------------------------
        stop_price	string
        -------------------------------------------------------------------
        side	string
        required: true
        buy or sell ***************************
        -------------------------------------------------------------------
        limit_price	string
        -------------------------------------------------------------------
        fill_type	string
        normal or immediate-or-cancel or fill-or-kill, default: normal
        -------------------------------------------------------------------
        expiration_time	integer
        Unix time Ms, default: null
        -------------------------------------------------------------------
        comment	string
        -------------------------------------------------------------------
        }
        :return:
        '''
        return self._post(
            '/trading/account/%s/order' % (self._account_ID),
            **params)

    def marketBuy(self, symbol: str, volume: str, comment: str, stopPrice: str):
        '''

        :param symbol:
        :param volume:
        :param comment:
        :param stopPrice:
        :return:
        [
          {
            "volume_initial": "0.01",
            "volume": "0.01",
            "time_created": 1577966281,
            "symbol": "ETHUSDd",
            "stop_price": "0.0",
            "side": "sell",
            "order_id": 135153,
            "limit_price": "228.7",
            "fill_type": "normal",
            "contract_size": "0.001",
            "comment": "order#8880"
          }
        ]
        '''
        return self.createOrder(
            symbol=symbol,
            side='buy',
            type='market',
            volume=str(volume),
            fill_type="immediate-or-cancel",
            comment=comment,
            stop_price=str(stopPrice)

        )

    def marketSell(self, symbol: str, volume: str, comment: str, stopPrice: str):
        '''

        :param symbol:
        :param volume:
        :param comment:
        :param stopPrice:
        :return:
        [
          {
            "volume_initial": "0.01",
            "volume": "0.01",
            "time_created": 1577966281,
            "symbol": "ETHUSDd",
            "stop_price": "0.0",
            "side": "sell",
            "order_id": 135153,
            "limit_price": "228.7",
            "fill_type": "normal",
            "contract_size": "0.001",
            "comment": "order#8880"
          }
        ]
        '''
        return self.createOrder(
            symbol=symbol,
            side='sell',
            type='market',
            volume=str(volume),
            fill_type="immediate-or-cancel",
            comment=comment,
            stop_price=str(stopPrice)
        )

    def buyLimit(self, symbol: str, volume: str, price: str, comment: str, stopPrice: str):
        '''

        :param symbol:
        :param volume:
        :param price:
        :param comment:
        :param stopPrice:
        :return:
        [
          {
            "volume_initial": "0.01",
            "volume": "0.01",
            "time_created": 1577966281,
            "symbol": "ETHUSDd",
            "stop_price": "0.0",
            "side": "sell",
            "order_id": 135153,
            "limit_price": "228.7",
            "fill_type": "normal",
            "contract_size": "0.001",
            "comment": "order#8880"
          }
        ]
        '''
        return self.createOrder(
            symbol=symbol,
            side='buy',
            type='limit',
            volume=str(volume),
            price=str(price),
            fill_type="immediate-or-cancel",
            comment=comment,
            stop_price=str(stopPrice)
        )

    def sellLimit(self, symbol: str, volume: str, price: str, comment: str, stopPrice: str):
        '''

        :param symbol:
        :param volume:
        :param price:
        :param comment:
        :param stopPrice:
        :return:
        [
          {
            "volume_initial": "0.01",
            "volume": "0.01",
            "time_created": 1577966281,
            "symbol": "ETHUSDd",
            "stop_price": "0.0",
            "side": "sell",
            "order_id": 135153,
            "limit_price": "228.7",
            "fill_type": "normal",
            "contract_size": "0.001",
            "comment": "order#8880"
          }
        ]
        '''
        return self.createOrder(
            symbol=symbol,
            side='sell',
            type='limit',
            volume=str(volume),
            price=str(price),
            fill_type="immediate-or-cancel",
            comment=comment,
            stop_price=str(stopPrice)
        )

    def deleteOrder(self, order_id: int):
        '''
        DELETE
        Order cancellation
        /trading/account/{account_id}/order/{order_id}
        :param order_id:
        :return:
        '''
        return self._delete(
            '/trading/account/%s/order/%s' % (self._account_ID, order_id)
        )

    def getAccountOrders(self):
        '''
        List orders by account login
        /trading/account/{account_id}/order
        :return:
        [
          {
            "volume_initial": "0.01",
            "volume": "0.01",
            "time_created": 1577966281,
            "symbol": "ETHUSDd",
            "stop_price": "0.0",
            "side": "sell",
            "order_id": 135153,
            "limit_price": "228.7",
            "fill_type": "normal",
            "contract_size": "0.001",
            "comment": "order#8880"
          }
        ]
        '''
        return self._get(
            'GET',
            '/trading/account/%s/order' % (self._account_ID)
        )







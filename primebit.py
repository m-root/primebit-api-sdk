import hmac
import hashlib
import requests
import time
import base64
import random
import string

BASE_URL = 'https://app.primebit.com/api/v1'


class PrimebitPublic():

    def __init__(self, type='live'):
        '''live or demo'''
        self.type = type
        self.base_url = BASE_URL

    def public_request(self, method, api_url, params=None):
        '''Public Requests'''
        r_url = self.base_url + api_url
        print(r_url)
        try:
            r = requests.request(method, r_url, params=params)
            print(r)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        if r.status_code == 200:
            return r.json()

    def _assetsDetails(self):
        '''

        :return:
        '''
        return self.public_request('GET', '/trading/assets')

    def assets(self):
        '''
        Details on crypto currencies available on the exchange
        /trading/assets
        :param params:
        :return:
        '''

        return [d for d in self._assetsDetails()]

    def symbols(self):
        '''
        Get symbols
        /trading/market_data/symbol/{type}
        :param params:
        :return:
        '''

        return self.public_request('GET', '/trading/market_data/symbol/%s' % (self.type))

    def symbolsDailyStats(self, symbol):
        '''
        Get symbol daily stats
        /trading/market_data/symbol/{type}/{symbol}/daily_stats
        :param params:
        :return:
        '''

        return self.public_request(
            'GET',
            '/trading/market_data/symbol/%s/%s/daily_stats' % (self.type, symbol)
        )

    def orderBook(self, symbol):
        '''
        Get aggregated 32-levels of order book
        /trading/market_data/order_book/{type}/{symbol}
        :param params:
        :return:
        '''
        return self.public_request(
            'GET',
            '/trading/market_data/order_book/%s/%s' % (self.type, symbol)
        )

    def getAllTicker(self):
        '''
        Overview of market data for all tickers
        /trading/market_data/summary/{type}
        :param params:
        :return:
        '''
        return self.public_request(
            'GET',
            '/trading/market_data/summary/%s' % (self.type)
        )

    def getTicker(self, symbol):
        '''
        Overview of market data for a symbol tickers
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
        return self.public_request(
            'GET',
            '/trading/market_data/ticker/%s' % (self.type)
        )

    def getTickerStat(self, symbol):
        '''
        24-hour rolling window price change statistics for a market
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
        return self.public_request(
            'GET',
            '/trading/market_data/trades/%s/%s' % (self.type, symbol)
        )

    def marketTradeCompleted(self, symbol):
        '''
        Trades completed in the last 10 minutes
        /trading/market_data/trades/{type}/last/{symbol}
        :param params:
        :return:
        '''
        return self.public_request(
            'GET',
            '/trading/market_data/trades/%s/last/%s' % (self.type, symbol)
        )


class PrimebitPrivate():
    def __init__(self, accountID=None, key=None, secret=None):

        self.base_url = BASE_URL
        self.key = bytes(key, 'utf-8')
        self.secret = bytes(secret, 'utf-8')
        self.accountID = bytes(accountID, 'utf-8')

    def order_link_id(self, stringLength):
        '''Alphanumeric random string generator'''
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

    def get_signed(self, sig_str):
        '''Parameter signing using sha512'''
        sig_str = base64.b64encode(sig_str)
        signature = base64.b64encode(hmac.new(self.secret, sig_str, digestmod=hashlib.sha256).digest())
        print(signature)
        return signature

    def signed_request(self, method, api_url, params=None):
        '''Handler for a signed requests'''

        param = ''
        if params:
            sort_pay = sorted(params.items())

            for k in sort_pay:
                param += '&' + str(k[0]) + '=' + str(k[1])
            param = param.lstrip('&')
        timestamp = str(int(time.time() * 1000))
        full_url = self.base_url + api_url

        if method == 'GET':
            if param:
                full_url = full_url + '?' + param
            sig_str = method + full_url + timestamp
        elif method == 'POST':
            sig_str = method + full_url + timestamp + param

        signature = self.get_signed(bytes(sig_str, 'utf-8'))

        headers = {
            'api-key': self.key,
            'authorization': signature,
            'timestamp': timestamp

        }
        print(headers)

        try:
            print(
                method,
                full_url,
                headers,
                params
            )
            r = requests.request(method, full_url, headers=headers, json=params)

            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
            print(r.text)
        if r.status_code == 200:
            return r.json()

    def getAllAccounts(self):
        '''
        GET
        /trading/account
        Get all user accounts

        :param params:
        :return:
        '''
        return self.signed_request(
            'GET',
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
        return self.signed_request(
            'GET',
            '/trading/account/%s' % (self.accountID)
        )

    def getAccountPositions(self):
        '''
        GET
        /trading/account/{account_id}/position
        List account positions

        :param params:
        :return:
        '''
        return self.signed_request(
            'GET',
            '/trading/account/%s/position' % (self.accountID)
        )

    def getPosition(self, symbol):
        '''
        GET
        /trading/account/{account_id}/position/{symbol}
        Get position

        :param params:
        :return:
        '''
        return self.signed_request(
            'GET',
            '/trading/account/%s/position/%s' % (self.accountID, symbol),
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
        return self.signed_request(
            'POST',
            '/trading/account/%s/order' % (self.accountID),
            **params)

    def marketBuy(self, symbol, volume, comment, stopPrice):
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
            # price=str(price),
            fill_type="immediate-or-cancel",
            comment=comment,
            stop_price=str(stopPrice)

        )

    def marketSell(self, symbol, volume, comment, stopPrice):
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

    def buyLimit(self, symbol, volume, price, comment, stopPrice):
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

    def sellLimit(self, symbol, volume, price, comment, stopPrice):
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

    def deleteOrder(self, order_id):
        '''
        DELETE
        Order cancellation
        /trading/account/{account_id}/order/{order_id}
        :param order_id:
        :return:
        '''
        return self.signed_request(
            'DELETE',
            '/trading/account/%s/order/%s' % (self.accountID, order_id)
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
        return self.signed_request(
            'GET',
            '/trading/account/%s/order' % (self.accountID)
        )

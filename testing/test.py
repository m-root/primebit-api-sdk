from primebit.primebit import PrimebitPrivate, PrimebitPublic


public = PrimebitPublic(type='live')

''' Details on crypto currencies available on the exchange'''

data = public.assets()
print(data)

''' Details on crypto currencies available on the exchange'''

data = public.assets()
print(data)

''' Get symbols'''

data = public.getsymbols()
print(data)

''' Get symbol daily stats'''


data = public.symbolsDailyStats(symbol='BTCUSD')
print(data)

''' Get aggregated 32-levels of order book'''

data = public.orderBook(symbol='BTCUSD')
print(data)

''' Overview of market data for all tickers'''

data = public.getAllTicker()
print(data)

''' Get data for a specific ticker'''

data = public.getTicker(symbol='BTCUSD')
print(data)

''' 24-hour rolling window price change statistics for all markets'''

data = public._tickersStats()
print(data)

''' 24-hour rolling window price change statistics for a specific pair'''

data = public.getTickerStat(symbol='BTCUSD')
print(data)

''' Trades completed in the last 24 hours for a given market.'''

data = public.getMarketTrades(symbol='BTCUSD')
print(data)

''' Trades completed in the last 10 minutes'''

data = public.marketTradeCompleted(symbol='BTCUSD')
print(data)

# ################################################################################################3

''' # Get all user accounts'''


Key = '6482d965-71e8-4d38-bec0-e2c72325835b'
Secret = 'o60jcowlM19wHQsmHoIG9sAMbRYWPP5a53CfaW5VeBg='
accountID = '510903ae-57ee-44b8-a1c8-a763d4eef930'
private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)

data = private.getAllAccounts()
for d in data:
    print(d)

'''Get account'''

private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.getAccount()
print(data)

''' List account positions'''

private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.getAccountPositions()
print(data)

''' Get a particular position '''

private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.getPosition(symbol='BTCUSD')
print(data)

''' Buy at market with a market order at current price '''

# private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
# data = private.marketBuy(symbol='BTCUSD', volume='0.001')
# print(data)

''' Sell at market with a market order at current price '''

private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.marketSell(symbol='BTCUSD', volume='0.001', comment='', stopPrice='')
print(data)

''' Buy Limit for an order '''

# private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
# data = private.buyLimit(symbol='ETHUSD', volume='0.001', price='7000')
# print(data)

''' Sell Limit for an order'''

private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.sellLimit(symbol='BTCUSD', volume='0.001', price='7000', comment='', stopPrice='')
print(data)

''' Cancel current pending orders '''

private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.deleteOrder(order_id=135153)
print(data)

''' Listing all orders'''

Key = '6482d965-71e8-4d38-bec0-e2c72325835b'
Secret = 'o60jcowlM19wHQsmHoIG9sAMbRYWPP5a53CfaW5VeBg='
accountID = '510903ae-57ee-44b8-a1c8-a763d4eef930'
# private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)

private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.getAccount()
print(data)




private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.createOrder(
    volume='0.005',
    type="limit",
    symbol="BTCUSDT",
    stop_price="0.0",
    side="buy",
    limit_price="7000.7",
    fill_type="immediate-or-cancel",
    comment="order#32787"
)
print(data)

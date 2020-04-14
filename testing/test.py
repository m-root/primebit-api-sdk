from primebit.primebit import PrimebitPrivate, PrimebitPublic

public = PrimebitPublic(type='live')

# Details on crypto currencies available on the exchange

data = public.assets()
print(data)

# Details on crypto currencies available on the exchange

data = public.assets()
print(data)

# Get symbols

data = public.getsymbols()
print(data)

# Get symbol daily stats


data = public.symbolsDailyStats(symbol='BTCUSD')
print(data)

# Get aggregated 32-levels of order book

data = public.orderBook(symbol='BTCUSD')
print(data)

# Overview of market data for all tickers

data = public.getAllTicker()
print(data)

# Get data for a specific ticker

data = public.getTicker(symbol='BTCUSD')
print(data)

# 24-hour rolling window price change statistics for all markets

data = public._tickersStats()
print(data)

# 24-hour rolling window price change statistics for a specific pair

data = public.getTickerStat(symbol='BTCUSD')
print(data)

# Trades completed in the last 24 hours for a given market.

data = public.getMarketTrades(symbol='BTCUSD')
print(data)

# Trades completed in the last 10 minutes

data = public.marketTradeCompleted(symbol='BTCUSD')
print(data)

################################################################################################3

# Get all user accounts


Key = 'a857c6bd-6fc2-40bb-967f-4c8e3f66e934'
Secret = 'XxWb5ilhctIYCsoi7N3Y66Der2fGP8qOuyNuRj0RWiA='
accountID = '976a8861-0a9f-4a2c-b383-99b8b158b6e4'
private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)

data = private.getAllAccounts()
print(data)

# Get account

private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.getAccount()
print(data)

# List account positions

private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.getAccountPositions()
print(data)

# Get a particular position

private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.getPosition(symbol='BTCUSD')
print(data)

# Buy at market with a market order at current price

private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.marketBuy(symbol='BTCUSD', volume='0.001', comment='', stopPrice='')
print(data)

# Sell at market with a market order at current price

private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.marketSell(symbol='BTCUSD', volume='0.001', comment='', stopPrice='')
print(data)

# Buy Limit for an order

private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.buyLimit(symbol='BTCUSD', volume='0.001', price='7000', comment='', stopPrice='')
print(data)

# Sell Limit for an order

private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.sellLimit(symbol='BTCUSD', volume='0.001', price='7000', comment='', stopPrice='')
print(data)

# Cancel current pending orders

private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.deleteOrder(order_id=135153)
print(data)

# Listing all orders

private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
data = private.getAccountOrders()
print(data)

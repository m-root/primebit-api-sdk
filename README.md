Account Endpoints
=================

Public Orders
------

Details on crypto currencies available on the exchange

.. code:: python


    from primebit import PrimebitPublic
    
    public = PrimebitPublic(type='live')
    data = public.assets()
    
    print(data)


Details on crypto currencies available on the exchange

.. code:: python


    from primebit import PrimebitPublic
    
    public = PrimebitPublic(type='live')
    data = public.assets()
    
    print(data)

Get symbols

.. code:: python


    from primebit import PrimebitPublic
    
    public = PrimebitPublic(type='live')
    data = public.getsymbols()
    
    print(data)

Get symbol daily stats

.. code:: python


    from primebit import PrimebitPublic
    
    public = PrimebitPublic(type='live')
    data = public.symbolsDailyStats(symbol='BTCUSD')
    
    print(data)

Get aggregated 32-levels of order book

.. code:: python


    from primebit import PrimebitPublic
    
    public = PrimebitPublic(type='live')
    data = public.orderBook(symbol='BTCUSD')
    
    print(data)

Overview of market data for all tickers

.. code:: python


    from primebit import PrimebitPublic
    
    public = PrimebitPublic(type='live')
    data = public.getAllTicker()
    
    print(data)



Get data for a specific ticker

.. code:: python


    from primebit import PrimebitPublic
    
    public = PrimebitPublic(type='live')
    data = public.getTicker(symbol='BTCUSD')
    
    print(data)


24-hour rolling window price change statistics for all markets

.. code:: python


    from primebit import PrimebitPublic
    
    public = PrimebitPublic(type='live')
    data = public._tickersStats()
    
    print(data)



24-hour rolling window price change statistics for a specific pair

.. code:: python


    from primebit import PrimebitPublic
    
    public = PrimebitPublic(type='live')
    data = public.getTickerStat(symbol='BTCUSD')
    
    print(data)




Trades completed in the last 24 hours for a given market.

.. code:: python


    from primebit import PrimebitPublic
    
    public = PrimebitPublic(type='live')
    data = public.getMarketTrades(symbol='BTCUSD')
    
    print(data)


Trades completed in the last 10 minutes
    
.. code:: python


    from primebit import PrimebitPublic
    
    public = PrimebitPublic(type='live')
    data = public.marketTradeCompleted(symbol='BTCUSD')
    
    print(data)



Private 
------


Get all user accounts

.. code:: python


    from primebit import PrimebitPrivate
    
    Key = ''
    Secret = ''
    accountID = ''
    
    private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
    data = private.getAllAccounts()
    
    print(data)

Get account
    
.. code:: python


    from primebit import PrimebitPrivate    
    
    Key = ''
    Secret = ''
    accountID = ''
    
    private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
    data = private.getAccount()
    print(data)

List account positions
    
.. code:: python


    from primebit import PrimebitPrivate    
    
    Key = ''
    Secret = ''
    accountID = ''
    
    private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
    data = private.getAccountPositions()
    print(data)

Get a particular position

.. code:: python


    from primebit import PrimebitPrivate
    
    Key = ''
    Secret = ''
    accountID = ''
    
    private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
    data = private.getPosition(symbol='BTCUSD')
    print(data)

Buy at market with a market order at current price

.. code:: python

    from primebit import PrimebitPrivate
    
    Key = ''
    Secret = ''
    accountID = ''
    
    private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
    data = private.marketBuy(symbol='BTCUSD', volume='0.001', comment='', stopPrice='')
    print(data)

Sell at market with a market order at current price

.. code:: python


    from primebit import PrimebitPrivate
    
    Key = ''
    Secret = ''
    accountID = ''
    
    private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
    data = private.marketSell(symbol='BTCUSD', volume='0.001', comment='', stopPrice='')
    print(data)



Buy Limit for an order

.. code:: python


    from primebit import PrimebitPrivate
    
    Key = ''
    Secret = ''
    accountID = ''
    
    private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
    data = private.buyLimit(symbol='BTCUSD', volume='0.001', price='7000', comment='', stopPrice='')
    print(data)


Sell Limit for an order
    
.. code:: python


    from primebit import PrimebitPrivate
    
    Key = ''
    Secret = ''
    accountID = ''
    
    private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
    data = private.sellLimit(symbol='BTCUSD', volume='0.001', price='7000', comment='', stopPrice='')
    print(data)



Cancel current pending orders 
    
.. code:: python


    from primebit import PrimebitPrivate
    
    Key = ''
    Secret = ''
    accountID = ''
    
    private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
    data = private.deleteOrder(order_id=135153)
    print(data)
    


Listing all orders 
    
.. code:: python


    from primebit import PrimebitPrivate
    
    Key = ''
    Secret = ''
    accountID = ''
    
    private = PrimebitPrivate(accountID=accountID, key=Key, secret=Secret)
    data = private.getAccountOrders()
    print(data)

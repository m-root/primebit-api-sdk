/////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////
PUBLIC
/////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////

Assets

GET
/trading/assets
Details on crypto currencies available on the exchange

++++++++++++++++++++++++++++++++++++++++++++++++
MarketData

GET
/trading/market_data/symbol/{type}
Get symbols

GET
/trading/market_data/symbol/{type}/{symbol}/daily_stats
Get symbol daily stats

++++++++++++++++++++++++++++++++++++++++++++++++
OrderBook

GET
/trading/market_data/order_book/{type}/{symbol}
Get aggregated 32-levels of order book


++++++++++++++++++++++++++++++++++++++++++++++++
Ticker

GET
/trading/market_data/summary/{type}
Overview of market data for all tickers

GET
/trading/market_data/ticker/{type}
24-hour rolling window price change statistics for all markets

++++++++++++++++++++++++++++++++++++++++++++++++
Trades

GET
/trading/market_data/trades/{type}/{symbol}
Trades completed in the last 24 hours for a given market.

GET
/trading/market_data/trades/{type}/last/{symbol}
Trades completed in the last 10 minutes.

/////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////
PRIVATE
/////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////

Order

GET
List orders by account login
/trading/account/{account_id}/order

------------------------------------------------
POST
Create new order
/trading/account/{account_id}/order

------------------------------------------------
DELETE
/trading/account/{account_id}/order/{order_id}
Cancel order

++++++++++++++++++++++++++++++++++++++++++++++++




Position

GET
/trading/account/{account_id}/position
List account positions

GET
/trading/account/{account_id}/position/{symbol}
Get position

Account

GET
/trading/account
Get all user accounts

GET
/trading/account/{id}
Get account

++++++++++++++++++++++++++++++++++++++++++++++++

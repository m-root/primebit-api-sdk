PRIMEBIT ENDPOINTS 
=================

Assets

    GET
    /trading/assets
    Details on crypto currencies available on the exchange


Get symbols

    GET
    /trading/market_data/symbol/{type}
    

Get symbol daily stats

    GET
    /trading/market_data/symbol/{type}/{symbol}/daily_stats



Get aggregated 32-levels of order book

    GET
    /trading/market_data/order_book/{type}/{symbol}



Overview of market data for all tickers

    GET
    /trading/market_data/summary/{type}
    Overview of market data for all tickers

24-hour rolling window price change statistics for all markets

    GET
    /trading/market_data/ticker/{type}


Trades completed in the last 24 hours for a given market.

    GET
    /trading/market_data/trades/{type}/{symbol}

Trades completed in the last 10 minutes.

    GET
    /trading/market_data/trades/{type}/last/{symbol}


PRIVATE
=================


List orders by account login

    GET
    /trading/account/{account_id}/order

Create new order

    POST
    /trading/account/{account_id}/order

Cancel order

    DELETE
    /trading/account/{account_id}/order/{order_id}


**Positions**

List account positions

    GET
    /trading/account/{account_id}/position

Get position

    GET
    /trading/account/{account_id}/position/{symbol}


**Account**

Get all user accounts

    GET
    /trading/account

Get account

    GET
    /trading/account/{id}



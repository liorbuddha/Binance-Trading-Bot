from binance.client import Client
from binance.enums import *

# API KEY, get from your account on binance
key1 = "WvrBN4oGcbJzFmcJAMlj7vqKcuFBida2U9M0RqprF1z5cdO8caZ2F0DQMzFSMtNu"
key2 = "BMlog6nC1hldS4YQcAlujVB5zFehkGjw9gffc1T77FjPqcJAmetiJeqvGyYpVDOo"
client = Client(key1, key2)


# set corrent price
def SetCorrrent(sym):
    corrent = client.get_recent_trades(symbol=sym)
    correntPrice = corrent[-1]
    correntPrice = correntPrice['price']
    correntPrice = float(correntPrice)
    return correntPrice


# set balance of selected wallet
def SetQty(sym):
    balance = client.get_asset_balance(asset=sym)
    balance = balance['free']
    balance = float(balance)
    balance *= 100
    balance = int(balance)
    balance = float(balance)
    balance /= 100
    return balance


# set price of last trade
def lastTrade(sym):
    trades = client.get_my_trades(symbol=sym)
    trades = trades[-1]
    trades = trades['price']
    trades = float(trades)
    return trades


# indicate is buyer or seller
def isBuyer(sym):
    buyer = client.get_my_trades(symbol=sym)
    buyer = buyer[-1]
    buyer = buyer['isBuyer']
    return buyer


# returns sub between trade[-1] and trade[-2]
def total(sym, i):
    totalTrade = client.get_my_trades(symbol=sym)
    totalTrade = totalTrade[-1*i]
    totalTrade = totalTrade['quoteQty']
    totalTrade = float(totalTrade)
    return totalTrade


class Trade:
    def sell(sym, qty):
        order = client.create_order(
            symbol=sym,
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            # timeInForce=TIME_IN_FORCE_GTC,
            quantity=qty,
            # price=SetCorrrent(sym='BNBUSDT'
        )

    def buy(sym, qty):
        order = client.create_order(
            symbol=sym,
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            # timeInForce=TIME_IN_FORCE_GTC,
            quantity=qty,
            # price=SetCorrrent(sym='BNBUSDT'
        )

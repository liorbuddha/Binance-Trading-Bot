from time import sleep
from binance.client import Client
from binance.enums import *
import config

## NEED TO ADD PROFIT

# VARIABLES
#  sym - symbol of trading
sym = 'BNBUSDT'
topValue = 2
vtopValue = topValue
floorValue = -1.4
vfloorValue = floorValue
# if starting from USDT set to False, if starting from BNB set to True
trade = config.isBuyer(sym)

# counters for buy and sell
bought = 0
sold = 0
# API KEY, get from your account on binance
# setup on config.py
client = Client(config.key1, config.key2)

# Balance, symb is the symbol of wallet you want to check
symb = 'BNB'
# set amount of trading coin (if trading BNBUSDT, take amount of BNB for buy and sell)
balance = config.SetQty(symb)

# GET INITIAL PRICE
# for fixed price, insert number
startPrice = config.lastTrade(sym)
print('start price is %s' % startPrice)
total = 0
x = 0
y = 0
z = 0

# price tracker
uphight = startPrice

isHigh = False
isLow = False

while True:  # -----  MAIN LOOP --------

    # Get corrent price
    correntPrice = config.SetCorrrent(sym)  # corrent
    print("corrent price is %s" % correntPrice)  # print(f"corrent price is {correctPrice}")

    while not trade:  # -------- WAITING TO BUY-------
        sleep(1)
        correntPrice = config.SetCorrrent(sym)  # Corrent
        # GOES UP      HOLDING USDT
        if correntPrice - startPrice >= 0:  # sold and price went up
            print(f"waiting for price to go down ", correntPrice, "bought", bought, "sold ", sold, "total ", total, "low ", floorValue, "high ", topValue)
        else:  # sold and price went down
            if correntPrice - startPrice <= floorValue:  # lower than floorValue
                correntPrice = config.SetCorrrent(sym)
                uphight = correntPrice
                floorValue = correntPrice - startPrice
                print('GOING DOWN!! ', correntPrice, "bought", bought, "sold ", sold, "total ", total, "low ", floorValue, "high ", topValue)
                print('new lowValue price: ', floorValue)
                isLow = True
            # not of the while
            # <0
            else:
                print("waiting for price to go down ", correntPrice, "bought", bought, "sold ", sold, "total ", total, "low ", floorValue, "high ", topValue)
                if uphight - correntPrice > 0.15 * floorValue and isLow == True:
                    bought += 1
                    # --------SET ORDER TO BUY--------
                    config.Trade.buy(sym, 0.4)
                    print("******************************************************")
                    print('B %s' % bought)
                    sleep(1)
                    startPrice = config.lastTrade(sym)
                    print("BOUGHT!!!!! ", startPrice)
                    print("******************************************************")
                    floorValue = vfloorValue
                    trade = True
                    isLow = False


    while trade:  # ------ WAITING FOR SELL--------
        correntPrice = config.SetCorrrent(sym)  # corrent
        if correntPrice <= startPrice:  # bought and price went down
            print("waiting for price to go up ", correntPrice, "bought", bought, "sold ", sold, "total ", total, "low ", floorValue, "high ", topValue)
        else:  # bought and price went up
            if (correntPrice - startPrice >= topValue) and (isHigh == False):
                correntPrice = config.SetCorrrent(sym)
                uphight = correntPrice
                topValue = correntPrice - startPrice
                print('GOING UP!! ', correntPrice, "bought", bought, "sold ", sold, "total ", total, "low ", floorValue, "high ", topValue)
                print('new upHigh price: ', uphight)
                isHigh = True
            else:
                print("waiting for price to go up ", correntPrice, "bought", bought, "sold ", sold, "total ", total, "low ", floorValue, "high ", topValue)
                if uphight - correntPrice > 0.15 * topValue and (isHigh == True):
                    sold += 1
                    # --------SET ORDER TO SELL--------
                    config.Trade.sell(sym, 0.4)
                    print("******************************************************")
                    print('S %s' % sold)
                    sleep(1)
                    startPrice = config.lastTrade(sym)
                    print("SOLD!!!!! ", startPrice)
                    print("******************************************************")
                    topValue = vtopValue
                    x = config.total(sym, 1)
                    y = config.total(sym, 2)
                    z = x - y
                    total += z
                    trade = False
                    isHigh = False

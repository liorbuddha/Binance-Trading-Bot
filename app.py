from time import sleep
from binance.client import Client
from binance.enums import *
import config
##-------CREATED BY LIOR BEN-ELIEZER-----------


# VARIABLES
#  sym - symbol of trading
sym = 'BNBUSDT'

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
balance = config.SetQty(symb)
# set amount of trading coin (if trading BNBUSDT, take amount of BNB for buy and sell)

# GET INITIAL PRICE
# for fixed price, insert number
startPrice = config.lastTrade(sym)
print('start price is %s' % startPrice)
sleep(3)
while True:  # -----  MAIN LOOP --------

    # Get corrent price
    correntPrice = config.SetCorrrent(sym)  # corrent
    print("corrent price is %s" % correntPrice)  # print(f"corrent price is {correctPrice}")

    while not trade:  # -------- WAITING TO BUY-------
        sleep(2)
        correntPrice = config.SetCorrrent(sym)  # Corrent
        # GOES UP
        if correntPrice - startPrice >= 0:
            print(f"waiting for price to go down ", correntPrice, "bought", bought, "sold ", sold)
            if correntPrice - startPrice >= 10:  # ---------------STEPPING UP
                bought += 1
                # --------SET ORDER TO BUY--------
                config.Trade.buy(sym, 0.48)
                print('B %s' % bought)
                sleep(1)
                startPrice = config.lastTrade(sym)
                print("BOUGHT!!!!! %s" % startPrice)
                trade = True
        else:
            if correntPrice - startPrice <= -0.012*startPrice:
                bought += 1
                # --------SET ORDER TO BUY--------
                config.Trade.buy(sym, 0.4)
                print('B %s' % bought)
                sleep(1)
                startPrice = config.lastTrade(sym)
                print("BOUGHT!!!!! %s" % startPrice)
                trade = True

            else:
                print("waiting for price to go down ", correntPrice, "bought", bought, "sold ", sold)

    while trade:  # ------ WAITING FOR SELL--------
        sleep(2)
        correntPrice = config.SetCorrrent(sym)  # corrent
        if correntPrice <= startPrice:
            print("waiting for price to go up ", correntPrice, "bought", bought, "sold ", sold)
            if correntPrice - startPrice <= -10:  # ----------STEPPING DOWN
                sold += 1
                # --------SET ORDER TO SELL--------
                config.Trade.sell(sym, 0.4)
                print('S %s' % sold)
                sleep(1)
                startPrice = config.lastTrade(sym)
                print("SOLD!!!!! %s" % startPrice)
                trade = False
        else:
            if correntPrice - startPrice >= 0.03*startPrice:
                sold += 1
                # --------SET ORDER TO SELL--------
                config.Trade.sell(sym, 0.5)
                print('S %s' % sold)
                sleep()
                startPrice = config.lastTrade(sym)
                print("SOLD!!!!! %s" % startPrice)
                trade = False
            else:
                print("waiting for price to go up ", correntPrice, "bought", bought, "sold ", sold)

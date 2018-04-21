import json
from cryptocompy import price
import datetime
import time
import numpy
import matplotlib.pyplot as plt

'''cryptocurrencies market data streaming'''
BTC_volume = [0]
BTC_time = [0]
ETH_volume = []
XRP_volume = []

starttime = time.time()

while True:
    #import cryptocurrency market volume
    coin_data = price.get_current_price(["BTC","ETH","XRP"], ["USD"],full = True)
    BTC_volume.append((coin_data['BTC']['USD']['LASTVOLUME']))

    #get time from data
    BTC_LASTUPDATE = (coin_data['BTC']['USD']['LASTUPDATE'])
    BTC_time_form = datetime.datetime.fromtimestamp(BTC_LASTUPDATE).strftime('%H%M')
    BTC_time.append(int(BTC_time_form))

    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

    print(BTC_volume)
    print(BTC_time)



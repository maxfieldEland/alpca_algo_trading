# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 10:57:19 2019

@author: mgreen13
"""
#API AUTHENTICATION
import numpy as np
import alpaca_trade_api as tradeapi
import matplotlib.pyplot as plt
import itertools
import datetime 
import seaborn as sns
from matplotlib import rc

rc('font',**{'family':'serif','serif':['Times']})
rc('text', usetex=True)

sns.set()
key_id = "PKLX9AL4V16WR215PTVO"
# retrieve secret key and close file
f = open("secret_key.txt","r")
if f.mode == 'r':
    secret_key = f.read()
f.close()


api = tradeapi.REST(key_id, secret_key, base_url = "https://paper-api.alpaca.markets")
account = api.get_account()
account.status
api.list_positions()
time = 300
def date_generator():
    from_date = datetime.datetime.today()
    while True:
        yield from_date
        from_date = from_date - datetime.timedelta(days = 1)
        

def time_series(symbol,time):

    dates = list(itertools.islice(date_generator(),time))
    
    # format date strings
    
    dates_clean = []
    for d in dates:
        dates_clean.append(d.isoformat().split("T")[0])
    
    dates_clean.reverse()
    barset = api.get_barset(symbol, 'day', limit=time)
    stock_bars = barset[symbol]
    week_open = np.zeros([time])
    for i in range(time):
        week_open[i] = stock_bars[i].o
    
    plt.figure(figsize = (15,10))
    plt.title("{} Timeseries from {} to {}".format(symbol,dates_clean[0],dates_clean[-1]),fontsize = 20)
    x = list(range(time))
    plt.plot(x,week_open)
    plt.ylabel("Value USD",fontsize = 17)
    plt.xlabel("Date",fontsize = 17)
    plt.xticks(x[0::7],dates_clean[0::7],rotation = 45,fontsize = 15)
    plt.yticks(fontsize = 15)
    plt.show()

symbol = "ETH"
length = 100
#symbol1 = str(input("What company would you like to construct a time series for?  "))
#length = int(input("How many days in the past would like to visualize?  "))
time_series(symbol,length)




import pandas as pd

import pandas_datareader.data as web

import datetime

import matplotlib 

import matplotlib.pyplot as plt

start = datetime.datetime(2023, 1, 1)

end = datetime.date.today()

stocklist=["01850.HK","03888.HK","06098.NS","SILV"]

prices=[]

for i in stocklist:

  f=web.DataReader(i, 'yahoo', start, end)

prices.append(f)

print (prices)
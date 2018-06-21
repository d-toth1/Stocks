''' Script imports stock data and presents
	them as graphs '''

import time
import datetime as dt
import os
width = os.get_terminal_size().columns

''' Import Packages '''
import pandas as pd
import pandas_datareader.data as pdr
import numpy as np
import matplotlib.pyplot as plt

''' Import Stock Data from Robinhood '''
aapl = pdr.get_data_robinhood('AAPL', start=dt.datetime(2017, 6, 20), end=dt.datetime(2018, 6, 20))
del aapl['session']

''' Export data '''
aapl.to_csv('aapl.csv')

''' Plot past year of data '''
aapl= aapl.astype(float)
aapl['close_price'].plot()
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('AAPL Closing Prices')

''' Gather Statistics on Stock '''
summary = aapl.describe()
print('********** Statistical Summary **********')
print(summary)
print('\n')
print(dt.datetime.now())
print('Created by D.W. Toth and J.D. Burns')

# plt.show()

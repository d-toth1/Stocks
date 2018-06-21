import time
import datetime as dt
import pandas as pd
import pandas_datareader.data as pdr
import numpy as np
import matplotlib.pyplot as plt
tickers = ['AAPL', 'AMD', 'SBUX']
def function(tickers):
	for i in tickers:
		x = pdr.get_data_robinhood(i, start=dt.datetime(2012, 6, 20), end=dt.datetime(2018, 6, 20))
		del x['session']
		x = x.astype(float)
		print(x)
		x['close_price'].plot()
		# plt.show()
		summary = x.describe()
		print(summary)
data = function(tickers)
print(data)

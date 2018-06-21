""" Script that functionally sorts through all
	possible stock tickers in the world-wide stock market.
	Writes tickers to a file if they exist in the database specified. """
	
import time
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
tickers = []
working_tickers = []
path = 'C:/Users/david/Documents/tickers.xlsx'
df = pd.read_excel(path)
# print(df['Ticker'])
list = df['Ticker'].tolist()
for i in list:
	tickers.append(str(i))
# print(tickers)
print("# of Tickers:", len(tickers))
def function(tickers):
	for i in tickers:
		try:
			x = web.DataReader(i, 'robinhood')
			del x['session']
			x = x.astype(float)
			print(x)
			x['close_price'].plot()
			# plt.show()
			summary = x.describe()
			print(summary)
			working_tickers.append(i)
			print(working_tickers)
			new_df = pd.DataFrame({'col': working_tickers})
			new_df.to_csv('workingtickers.csv')
		except:
			print("Failed")
			pass
data = function(tickers)
print(data)

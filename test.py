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
etf = []
etf_working = []
path = 'C:/Users/david/Documents/tickers.xlsx'
df = pd.read_excel(path)
xlsx = pd.ExcelFile(path)
df_xlsx = pd.read_excel(xlsx, 'ETF')
etf_list = df_xlsx['Ticker'].tolist()
# print(df['Ticker'])
list = df['Ticker'].tolist()
for i in list:
	tickers.append(str(i))
for i in etf_list:
	etf.append(str(i))
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
def function2(etf):
	for i in etf:
		try:
			y = web.DataReader(i, 'robinhood')
			del y['session']
			y = y.astype(float)
			print(y)
			y['close_price'].plot()
			# plt.show()
			summary = y.describe()
			print(summary)
			etf_working.append(i)
			print(etf_working)
			new_df2 = pd.DataFrame({'col': etf_working})
			new_df2.to_csv('etfworking.csv')
		except:
			print("Failed")
			pass

# data = function(tickers)
data2 = function2(etf)
# print(data)
print(data2)

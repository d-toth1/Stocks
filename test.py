import time
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
tickers = ['AMD']
working_tickers = []
path = 'C:/Users/david/Documents/tickers.xlsx'
df = pd.read_excel(path)
print(df['Ticker'])
list = df['Ticker'].tolist()
for i in list:
	tickers.append(str(i))
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
			new_tickers.append(i)
			print(new_tickers)
			new_df = pd.DataFrame({'col': working_tickers})
			new_df.to_csv('workingtickers.csv')
		except:
			print("Failed")
			pass
data = function(tickers)
print(data)

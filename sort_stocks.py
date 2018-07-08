"""
Script that functionally sorts through all
possible stock tickers in the world-wide stock market.
Writes tickers to a file if they exist in the database specified (Robinhood). 
"""

from imports import *

path = 'C:/Users/david/Documents/tickers.xlsx'
tickers = []
working_tickers = []
etf = []
etf_working = []

df = pd.read_excel(path)
list = df['Ticker'].tolist()

xlsx = pd.ExcelFile(path)
df_xlsx = pd.read_excel(xlsx, 'ETF')
etf_list = df_xlsx['Ticker'].tolist()

for i in list:
	tickers.append(str(i))
for i in etf_list:
	etf.append(str(i))
print("# of Tickers:", len(tickers))
print("# of ETF's:", len(etf))

def get_ticker(tickers):
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

def get_etf(etf):
	for i in etf:
		try:
			y = web.DataReader(i, 'robinhood')
			del y['session']
			y = y.astype(float)
			print(y)
			summary = y.describe()
			print(summary)
			etf_working.append(i)
			print(etf_working)
			new_df2 = pd.DataFrame({'col': etf_working})
			new_df2.to_csv('etfworking.csv')
		except:
			print("Failed")
			pass

# ticker_data = get_ticker(tickers)
# etf_data = get_etf(etf)
# print(ticker_data)
# print(etf_data)

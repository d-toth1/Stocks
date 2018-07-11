from imports import *

root = Tk ()
root.title("JBDT Stocks Software")
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

user = ''
password = ''
david = ''
jonathan = ''

class Stocks:
	def __init__(self, root):
		self.top_label = Label(root, text = "JD Stock Trading Software")
		self.top_label.configure(font=(18))
		self.top_label.grid(column=1, row=0, columnspan=2, sticky=(N))
		self.ImportStocksButton = Button(root, text="Import Stocks", command = self.ImportStocks)
		self.ImportStocksButton.configure(width =15)
		self.ImportStocksButton.grid(column=0, row=1, sticky=(N))
		self.ViewTrendButton = Button(root, text="Trends", command = self.ViewTrends)
		self.ViewTrendButton.configure(width = 15)
		self.ViewTrendButton.grid(column=1, row=1, sticky=(N))
		self.StockStatsButton = Button(root, text="Statistics", command = self.Stats)
		self.StockStatsButton.configure(width = 15)
		self.StockStatsButton.grid(column=2, row=1, sticky=(N))
		self.TestNotification = Button(root, text = "IFTTT Test", command = self.Notify)
		self.TestNotification.configure(width=15)
		self.TestNotification.grid(column=3, row=1, sticky=(N))
		self.ProgressBar = Progressbar(root, orient = HORIZONTAL, length = 100)
		self.ProgressBar.configure(mode='indeterminate')
		self.ProgressBar.grid(column=1, row=2, columnspan=2, sticky= 'w',pady = 5)
		self.ProgressBarLabel = Label(root, text='Progress:')
		self.ProgressBarLabel.grid(column=0, row=2, columnspan=2, sticky='w')

	def ImportStocks(self):
		etf_path = "C:/Users/david/Stocks/Data/etfworking.xlsx"
		ticker_path = "C:/Users/david/Stocks/Data/workingtickers.xlsx"
		tickerxlsx = pd.ExcelFile(ticker_path)
		tickers = pd.read_excel(tickerxlsx)
		etfxlsx = pd.ExcelFile(etf_path)
		etfs = pd.read_excel(etfxlsx)
		ticker_list = tickers['TICKER'].tolist()
		etf_list = etfs['ETF'].tolist()
		print(ticker_list)
		print(etf_list)

	def ViewTrends(self):
		pass

	def Stats(self):
		pass

	def Notify(self):
		# david_url = 'https://maker.ifttt.com/trigger/test_event/with/key/dEd4zv7UNm4oLjt1tIqQza'
		# jonathan_url = 'https://maker.ifttt.com/trigger/test_event/with/key/noHcDtIOVbiAOOIuVCLC-zPpp4rf1A5dbLiEex5qbaW'
		# self.ProgressBar.start()
		# requests.post(david_url)
		# requests.post(jonathan_url)
		# messagebox.showinfo(title="Test Notification", message = "Notification sent to mobile app")
		# self.ProgressBar.stop()
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(user, password)
		server.sendmail(user, '', 'Hello')
		server.sendmail(user, jonathan, 'Hello, Jonathan. This message is sent from Python. - David')
		server.quit()

GUI = Stocks(root)
root.mainloop()

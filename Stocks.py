from imports import *

class Stocks:
	def __init__(self, master):
		self.master = master
		master.title("JD Stocks")
		self.top_label = Label(master, text = "JD Stock Trading Software")
		self.top_label.configure(font=(18))
		self.top_label.configure(background='white')
		self.top_label.pack()
		self.ImportStocksButton = Button(master, text="Import Stocks", command = self.ImportStocks)
		self.ImportStocksButton.configure(width =10)
		self.ImportStocksButton.pack()
		self.ViewTrendButton = Button(master, text="Trends", command = self.ViewTrends)
		self.ViewTrendButton.configure(width = 10)
		self.ViewTrendButton.pack()
		self.StockStatsButton = Button(master, text="Statistics", command = self.Stats)
		self.StockStatsButton.configure(width = 10)
		self.StockStatsButton.pack()
		self.TestNotification = Button(master, text = "IFTTT Test", command = self.Notify)
		self.TestNotification.configure(width=10)
		self.TestNotification.pack()
		self.img = 'C:/Users/david/OneDrive/Pictures/Capture.PNG'
		self.window_image = ImageTk.PhotoImage(Image.open(self.img))
		self.window_image_label = Label(master, image = self.window_image)
		self.window_image_label.configure(background='white')
		self.window_image_label.pack()

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
		david_url = 'https://maker.ifttt.com/trigger/test_event/with/key/dEd4zv7UNm4oLjt1tIqQza'
		jonathan_url = 'https://maker.ifttt.com/trigger/test_event/with/key/noHcDtIOVbiAOOIuVCLC-zPpp4rf1A5dbLiEex5qbaW'
		requests.post(david_url)
		requests.post(jonathan_url)
		messagebox.showinfo(title="Test Notification", message = "Notification sent to mobile app")

root = Tk ()
GUI = Stocks(root)
root.configure(background = 'white')
root.geometry('400x400')
root.mainloop()

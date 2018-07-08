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
		img = 'C:/Users/david/OneDrive/Pictures/Capture.PNG'
		self.window_image = ImageTk.PhotoImage(Image.open(img))
		self.window_image_label = Label(master, image = self.window_image)
		self.window_image_label.configure(background='white')
		self.window_image_label.pack()

	def ImportStocks(self):
		pass

	def ViewTrends(self):
		pass

	def Stats(self):
		pass

	def Notify(self):
		david_url = 'https://maker.ifttt.com/trigger/test_event/with/key/dEd4zv7UNm4oLjt1tIqQza'
		jonathan_url = 'https://maker.ifttt.com/trigger/test_event/with/key/noHcDtIOVbiAOOIuVCLC-zPpp4rf1A5dbLiEex5qbaW'
		requests.post(david_url)
		# requests.post(jonathan_url)
		messagebox.showinfo(title="Test Notification", message = "Notification sent to mobile app")

root = Tk ()
GUI = Stocks(root)
root.configure(background = 'white')
root.geometry('250x250')
root.mainloop()

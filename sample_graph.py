""" Script imports stock data and presents
	them as graphs """

import time
import datetime as dt
now = dt.datetime.now()
t0 = time.clock()
#Imports packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("Packages imported")
t1 = time.clock()
total_time = t1-t0
print("Script time:", total_time)

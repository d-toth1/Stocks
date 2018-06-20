""" Script to gather data from stock market """
#Packages to import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("All packages imported")

list = []
for i in range(100):
    list.append(i)

print(list)

x = list
y = []
for i in range(100):
    j = i**2
    y.append(j)

print(y)

x_np = np.array(x)
y_np = np.array(y)

plt.plot(x_np, y_np)
plt.show()

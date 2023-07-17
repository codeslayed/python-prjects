
import numpy
import pandas as pd
columns = ["E1", "Q2", "px2", "M", "eta2"]
data = pd.read_csv('dielectron.csv', usecols=columns)






import matplotlib.pyplot as plt
xaxis = (data.E1, data.px2)
yaxis = (data.eta2 ,data.M)
plt.plot(xaxis, yaxis)
plt.show()
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as pl


url="loadtext.txt"
names=['first value','second value']
dataset=pandas.read_csv(url,names=names)
print(dataset.shape)
print(dataset.head(6))
dataset.plot(kind='line',subplots=True,layout=(2,2),sharex=False,sharey=False)
pl.show()

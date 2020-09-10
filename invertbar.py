import matplotlib.pyplot as pl

x=[1,2,3,4,5]
y=[12,5,69,50,40]

tick_label=["India","America","China","Russia","Japan"]


pl.barh(x,y,tick_label=tick_label,color=["red","green","blue"])
pl.xlabel("cont")
pl.ylabel("data")
pl.title("populations")
pl.show()

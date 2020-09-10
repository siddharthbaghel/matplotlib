import matplotlib.pyplot as pl

x=[1,2,3,4,5]
y=[12,5,69,50,40]

ticklabel=["India","America","China","Russia","Japan"]


pl.bar(x,y,tick_label=ticklabel,width=0.5,color=["red","green","blue"])
pl.xlabel("cont")
pl.ylabel("data")
pl.title("populations")
pl.show()

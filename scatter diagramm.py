import matplotlib.pyplot as pl

x=[1,2,3,4,5,6,7,8]
y=[5,4,2,7,9,4,6,8]

pl.scatter(x,y,label='my scatter',color='m',s=500,marker="*")

## in a marker we can also use +,x,. in place of marker. by defalut it is (.).
## symbol s stands for size

pl.title("interesting graph\ncheck it out")
pl.xlabel("X-axis")
pl.ylabel("Y-axis")
pl.show()

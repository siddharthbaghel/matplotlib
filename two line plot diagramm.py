import matplotlib.pyplot as pl

x=[1,2,3,4,5]
y=[2,34,6,8,10]

x2=[1,2,3,4,5]
y2=[10,20,30,40,50]

pl.plot(x,y,label='first line',color='r')
pl.plot(x2,y2,label='second line')

pl.title("interesting graph\ncheck it out")
pl.xlabel("plot number")
pl.ylabel("importent var")
pl.legend()
pl.show()

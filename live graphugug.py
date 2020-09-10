import matplotlib.pyplot as pl
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

style.use('fivethirtyeight')

fig=pl.figure()

ax1=fig.add_subplot(1,1,1)



def animate(i):
    x=[]
    y=[]
    x,y=np.loadtxt('loadtext.txt',delimiter=',',unpack=True)
    
    ax1.clear()
    ax1.plot(x,y)

ani=animation.FuncAnimation(fig,animate,interval=1000)

pl.show()
    

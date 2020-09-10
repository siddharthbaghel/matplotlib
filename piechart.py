import matplotlib.pyplot as pl



slices=[7,2,3,13]
activities=['sleeping','eating','working','playing']
cols=['c','m','r','b']
pl.pie(slices,labels=activities,colors=cols,startangle=348,shadow=True,
       explode=(0,0,0.1,0),autopct='%1.1f%%')

pl.title('interesting graph\ncheck it out')

###pl.legend()

pl.show()

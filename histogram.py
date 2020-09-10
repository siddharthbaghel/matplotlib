import matplotlib.pyplot as pl

ages=[17,19,25,66,89,43,78]

#bins=[x for x in range(0,len(ages))]

bins=[10,20,30,40,50,60,70,80,90,100]

pl.hist(ages,bins,histtype='bar',color='red',rwidth=0.8)

pl.title("interesting graph\ncheck it out")
pl.xlabel("ages")
pl.ylabel("distribution")
pl.show()

from matplotlib import pyplot as plt
import numpy as np

#syntax= plt.pie(sizes,colors,labels,shadow,explode)
#explode= it take out a specific part of pie chart
#shadow=shadow is a form for pie chart to look i a 3-D way
hours=[2,6,1,4,2,6,2,1]
activity=["ready","school","rest","study","play","sleep","tv","yoga"]
explodes=[1,0,0,0,0,0,0,1]#1 is the size(how much you want to take out a specific part)you can use any no. for size like 0.2 etc.
#'''color=["red"] check this out you will understand'''
plt.pie(hours,labels=activity,shadow=True,explode=explodes)
plt.show()

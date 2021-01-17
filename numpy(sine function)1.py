from matplotlib import pyplot as plt 
import numpy as np

x = np.arange(-10,10, 0.1)
'''basically its an array which will give us point between -10 to 10 in graph
so there would be total 20 points with a gap of 0.1 between each point
so there would be total 200 points(20/0.1)
print(len(x))=200'''
y = np.sin(x)


plt.plot(x,y)
plt.show()


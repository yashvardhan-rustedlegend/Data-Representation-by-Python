from matplotlib import pyplot as plt
import numpy as np


x=[i for i in range (10)]
y=[4,1,7,2,9,0,12,5,6,8]
x2=[i+0.2 for i in range(10)]
z=[4,3,5,6,7,4,5,10,5,3]
plt.bar(x,y,color="blue",width=0.2,label="2017")
plt.bar(x2,z,color="red",width=0.2, label="2018")#this function is used to represent bar graph
plt.legend()#this fubnction is required for label to print without this label cant be printed
plt.show()




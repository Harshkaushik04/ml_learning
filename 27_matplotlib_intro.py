import matplotlib.pyplot as plt
import numpy as np
x=np.arange(10)
y=2*x
#print(x,y)
plt.plot(x,y) #plotting x array s' elements vs y array s' elements
plt.title('Data analysis') #title
plt.xlabel('x-axis')#x label
plt.ylabel('y-axis')#y label
plt.xlim(0,6)#plot between x=0 and 6
plt.ylim(0,15)#plt between y=0 and 15
plt.savefig('/home/harsh/graph/my_first_plotz.png') #saving figure inside a particular location
plt.show()#for showing plot

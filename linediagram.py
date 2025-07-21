import matplotlib.pyplot as plt 
import numpy as np
x=np.array([1,2,6,18])
y=np.array([3,10,12,20])
plt.plot(x,y,marker='o',mec='green',mfc='green',color='red',linestyle='dotted')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title("plotted diagram")
plt.show()

import matplotlib.pyplot as plt 
x=([1,2,6,18])
y=([3,10,12,20])
x1=([15,10,7,4])
y1=([14,13,9,5])
plt.plot(x,y,marker='o',mec='green',mfc='green',color='red',linestyle='dotted',label="line1")
plt.plot(x1,y1,marker='o',mec='green',mfc='green',color='red',linestyle='dotted',label="line2")
plt.legend()
plt.show()

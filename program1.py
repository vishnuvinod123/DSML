import numpy as np
a=np.array([[1,2,3],[3,6,7],[7,3,2]])
print (a)
s=np.sum(a,axis=0)
print("sum of column=",s)
s=np.sum(a,axis=1)
print("sum of raw=",s)


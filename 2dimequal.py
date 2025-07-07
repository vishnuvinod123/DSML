import numpy as np
a=np.array([[1,2,3],[3,6,7],[7,3,2]])
print (a)
b=np.array([[1,2,3],[2,4,0],[10,5,2]])
print(b)
if np.array_equal(a,b):
	print("equal")
else:
	print("not equal")

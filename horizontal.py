import matplotlib.pyplot as plt
import numpy as np
languages=['java','pthon','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8.9,7.7,6.7]
x=np.array(languages)
y=np.array(popularity)
colors=['blue','brown','green','orange','red','yellow']
plt.barh(x,y,color=colors)
plt.xlabel("languages")
plt.ylabel("popularity")
plt.show()

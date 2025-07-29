import pandas as pd
mylist={'name':['alice','bob','charlie'],
		'age':[25,30,35],
		'score':[88,76,91]
	}
df=pd.DataFrame(mylist)
result=df.head(2)
print(result)

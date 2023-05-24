import pandas as pd
data = {'sales1':[10,20,-4,5,-1,15],
'sales2':[20,15,10,-1,12,-2]}
df = pd.DataFrame(data)
print("Data Frame")
print(df)
print('Display DataFrame after replacing every negative value with 0')
df[df<0]=0
print(df)
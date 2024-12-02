import pandas as pd
from collections import defaultdict
df=pd.read_csv('data.txt',delimiter=r'\s+',header=None)
df.columns=['c1','c2']
hashmap=defaultdict(lambda:0)

df['c1'] = df['c1'].sort_values().values
df['c2'] = df['c2'].sort_values().values



for i in range(len(df)):
    hashmap[df['c2'][i]]+=1

res=0
for i in range(len(df)):
    res+=(df['c1'][i]*hashmap[df['c1'][i]])
print(res)
import pandas as pd
import numpy as np

df=pd.read_csv("input.txt", delimiter=r'\s+', header=None)

arr=df.values.tolist()

def is_sorted(arr):
    arr = [x for x in arr if not np.isnan(x)]
    return arr==sorted(arr) or arr==sorted(arr, reverse=True)

def is_valid(arr):
    arr = [x for x in arr if not np.isnan(x)]
    for i in range(len(arr)-1):
        diff = abs(arr[i+1]-arr[i])
        if(diff>3 or diff<1):
            return False
    return True
            
res=0
for i in range(len(arr)):
    if(is_sorted(arr[i]) and is_valid(arr[i])):
        res+=1
        
print(res)

#Part 1 : 359



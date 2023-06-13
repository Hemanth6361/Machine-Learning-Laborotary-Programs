import pandas as pd
import numpy as np
data=pd.read_csv("dataset.csv")
print(data)
d=np.array(data)[:,:-1]
print(d)
print(d[0][1])
print(d[0][2])
print()

t=np.array(data)[:,-1]
print(t)
for i in range(len(t)):
    if t[i]=="Yes":
        h0=np.array(d[i])
        k=i
        break
print(h0)
print()
for k in range(len(t)):
    h1=np.array(d[k])
    if t[k]=="Yes":
        for p in range(len(h0)):
            if (h0[p]!=h1[p]):
                h1[p]="?"
                
                print(h1)
            else:
                pass

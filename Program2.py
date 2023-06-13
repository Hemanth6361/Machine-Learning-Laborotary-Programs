import pandas as pd
import numpy as np
data=pd.read_csv("dataset.csv")
print(data)
d=np.array(data)[:,:-1]
print(d)

t=np.array(data)[:,-1]
print(t)
print("-----------------------------------------------------")
g=np.array([' ? ',' ? ',' ? ',' ? ',' ? ',' ? '])
p=np.array(g)

for i in range(len(t)):
    if t[i]=="Yes":
        s=np.array(d[i])
        
        break
print(s)
print("-----------------------------------------------------")

print('Final general hypotesis:')

for i in range(len(t)):
    if t[i]=="Yes":
        for x in range(len(s)):
            if s[x]!=d[i][x]:
                s[x]='?'
    elif t[i]=="No":
        for y in range(len(d)):
            if d[i][y]!=s[y]:
                if s[y]!="?":
                    g[y]=s[y]
                   
                    print(g)
                    g[y]=p[y]
                else:
                    pass
   
    else:
        pass
print("-----------------------------------------------------")
print('Final specific hypothesis:',s)

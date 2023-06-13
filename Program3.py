import pandas as pd
data = pd.read_csv('dataset.csv')
print(data)

data1 = data.drop_duplicates(subset=['Reg'])
print(data1)

for i in data1.columns:
    if(len(data1[i].dropna().unique()) == 1):
        column_sv = []
        column_sv.append(i)

print(column_sv)
print(data1.drop(column_sv,axis=1))

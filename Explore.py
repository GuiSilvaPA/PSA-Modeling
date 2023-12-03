import pandas as pd
import matplotlib.pyplot as plt

path = 'D:/Modeling/vars.csv'

data = pd.read_csv(path)
orig = len(data)

data = data[data['A_CODE'] == 0]
data = data[data['A_RCFC'] >= 0.02]
data = data[data['ISLD_I2'].isna()]

cols = []
for col in data.columns[:25]:
    cols.append(col)

for col in data.columns[47:59]: 
    cols.append(col)

data = data[cols].reset_index(drop=True)

fina = len(data)

# print(100*fina/orig)
# print(fina)
# print(fina/119)

# 705 / 1771

print(data)

print(len(data[data['Contigence'].isin([i for i in range( 1, 17)])]))
print(len(data[data['Contigence'].isin([i for i in range(17, 52)])]))
print(len(data[data['Contigence'].isin([i for i in range(52, 120)])]))

# data = data[data['Contigence'].isin([i for i in range(52, 120)])]

data = data[data['A_NDRC'] < 0.02]

plt.hist(data['A_NDRC'], bins=50)
plt.show()
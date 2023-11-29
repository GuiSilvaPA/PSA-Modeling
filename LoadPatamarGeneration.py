import numpy.random as rnd
import numpy  as np
import pandas as pd

data = []
for i in range(10, 120):
    for j in range(5):

        low  = (i-5)/100
        high = (i+5)/100

        a = list(rnd.uniform(low=low, high=high, size=35))
        a.append(np.mean(a))
        a.append(i)

        data.append(a)


txt_cols = 'B17,B18,B20,B21,B23,B24,B25,B26,B27,B28,B29,B33,B36,B39,B40,B41,B42,B44,B45,B46,B47,B48,B49,B50,B51,B52,B53,B55,B56,B59,B60,B61,B64,B67,B68,Total,Carregamento'
cols = txt_cols.split(',')

data = pd.DataFrame(data, columns=cols)
data.to_csv('D:/Modeling/BASE/CARGA.csv', index=False)
print(data)
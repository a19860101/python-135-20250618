import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font',family='Microsoft Jhenghei')

# datas = pd.read_csv('./travel.csv',header=1)
datas = pd.read_csv('./travel.csv',header=0)

d = datas.iloc[1][2:-1]
label = datas.columns[2:-1]

print(label)
plt.pie(d, labels=label)

plt.show()

print(d)
print(datas)
print(datas.columns)



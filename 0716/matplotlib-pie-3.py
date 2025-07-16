import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font',family='Microsoft Jhenghei')

# datas = pd.read_csv('./travel.csv',header=1)
datas = pd.read_csv('./travel.csv',header=0)

d = list(datas.iloc[1][2:-1])
label = list(datas.columns[2:-1])
label.append('其他國家')

print(datas)
# print(datas.iloc[1]['亞洲地區'])
# print(datas.iloc[1]['小計'])
other = int(datas.iloc[1]['亞洲地區']) - int(datas.iloc[1]['小計'])

d.append(other)
d = [int(item) for item in d]

print(d)

plt.pie(d, labels=label, autopct='%.1f%%')

plt.show()




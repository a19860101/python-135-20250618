import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font',family='Microsoft Jhenghei')

data = pd.read_csv('./travel.csv')

print(data)

d = data.iloc[1][2:-1]

print(d.index.tolist())
print(d.values.tolist())

y = [int(item) for item in d.values.tolist()]
color = 'pink'

plt.bar(d.index.tolist(),y,color=color)

plt.show()

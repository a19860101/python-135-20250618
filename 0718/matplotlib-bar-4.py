import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font',family='Microsoft Jhenghei')

data = pd.read_csv('./travel2.csv')

print(data)

y112 = data.iloc[1][2:-1]
y112 = [int(item) for item in y112.values.tolist()]

y113 = data.iloc[2][2:-1]
y113 = [int(item) for item in y113.values.tolist()]

label = data.columns[2:-1]
x1 = [1,2,3,4,5,6,7,8,9]
x2 = [item - 0.2 for item in x1]

plt.bar(x1, y112, width=.4, align='edge', label='112年')
plt.bar(x2, y113, width=.4, label='113年')

plt.xticks(range(1,10),label)
plt.legend()
plt.show()

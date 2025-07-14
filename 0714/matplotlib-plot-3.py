import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font', family='Microsoft Jhenghei')


data = pd.read_csv('FMSRFK_2330_2025.csv', encoding='big5', header=1)

print(data['最高價'])

max_ = list(data['最高價'])

# d = []

max_ = [float(i.replace(',','')) for i in max_[:6]]

min_ = [float(i.replace(',','')) for i in list(data['最低價'])[:6]]

# for i in max_[:6]:
#     i = i.replace(',','')
#     i = float(i)
#     d.append(i)
# print(d)

print(max_)
#
dataX = range(1,7)

plt.plot(dataX, max_, label='最高價',color='red',marker='.')
plt.plot(dataX, min_, label='最低價',color='green', marker='.')
plt.ylim(700,1500)
plt.xticks(range(1,7))
plt.legend()
plt.show()
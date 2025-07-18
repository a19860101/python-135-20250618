import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font',family='Microsoft Jhenghei')

datas = pd.read_csv('./animal.csv')

total, col = datas.shape

dog = len(datas[datas['animal_kind'] == '狗'])
cat = len(datas[datas['animal_kind'] == '貓'])

other = total - (dog + cat)

data = [dog, cat, other]
label = ['狗', '貓', '其他動物']
plt.pie(data, labels=label, autopct='%.1f%%', explode=[0,0,.2])
plt.show()
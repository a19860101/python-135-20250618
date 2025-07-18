import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font',family='Microsoft Jhenghei')

data = pd.read_csv('./animal.csv')

other = data[data['animal_kind'].str.contains('狗|貓') == False]

d = other['animal_Variety'].value_counts()

print(d)

plt.pie(d.values, labels=d.index, autopct='%.2f%%')

plt.show()
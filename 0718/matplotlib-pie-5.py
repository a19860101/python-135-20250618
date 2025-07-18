import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font',family='Microsoft Jhenghei')

data = pd.read_csv('./animal.csv')

dogs = data[data['animal_kind'] == '狗']

# print(dogs['animal_Variety'])
dog_variety = dogs['animal_Variety'].nunique()

# d = dogs['animal_Variety'].value_counts(ascending=True)
d = dogs['animal_Variety'].value_counts()

# print(d.index)
# print(d.values)

# print(d.index.tolist())
# print(d.values.tolist())

plt.pie(d.values, labels=d.index)

plt.show()
import pandas as pd

users = pd.DataFrame([
    {'name': 'Zac', 'age': '32', 'gender': 'M'},
    {'name': 'Max', 'age': '28', 'gender': 'M'},
    {'name': 'Andy', 'age': '30', 'gender': 'M'},
    {'name': 'Amy', 'age': '22', 'gender': 'F'},
    {'name': 'Laura', 'age': '26', 'gender': 'F'}
])
numberAge = [int(a) for a in users['age']]

# for a in users['age']:
#     numberAge.append(int(a))

print(numberAge)

age = pd.Series(numberAge)

print(age)
print(age.min())
print(age.max())
print(age.median())
print(age.mean())
print(age.std())
print(age.describe())
#
# print(users['age'])
# print(users['age'].min())
# print(users['age'].max())
# print(users['age'].median())
# print(users['age'].mean())
# print(users['age'].std())
# print(users['age'].describe())
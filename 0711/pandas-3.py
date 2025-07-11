import pandas as pd

users = pd.DataFrame([
    {'name': 'Zac', 'age': 32, 'gender': 'M'},
    {'name': 'Max', 'age': 28, 'gender': 'M'},
    {'name': 'Andy', 'age': 30, 'gender': 'M'},
    {'name': 'Amy', 'age': 22, 'gender': 'F'},
    {'name': 'Laura', 'age': 26, 'gender': 'F'}
])


condition = users['age'] > 25

# print(users[condition])
# print(users[users['age'] >= 30])
# print(users[users['gender'] == 'M'])

# male = users[users['gender'] == 'M']
# female = users[users['gender'] == 'F']

# print(male)
# print(female)

print(users[users['name'].str.contains('A&a')])
import pandas as pd

data = pd.read_json('TransService.json')

print(data.iloc[0])

# data = data[data['shelter_address'].str.contains('臺北市')]
# data = data[data['animal_kind'] == '狗']
data = data[data['animal_Variety'].str.contains('柴')]

data = data[['animal_kind','animal_Variety','animal_opendate','shelter_address']]
data.columns = ['種類','品種','領養日期','地址']

data.to_excel('animal.xlsx')

print(data)
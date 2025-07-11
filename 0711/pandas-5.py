import pandas as pd

data = pd.read_csv('Restaurant_C_f.csv')

print(data.iloc[0])

# print(data[data['Region']=='新北市'])
# print(data[data['Add'].str.contains('新北')])

myDatas = data[data['Add'].str.contains('新北')]
# ty = data[data['Region'] == '桃園市']
# print(sb['Name'])
# print(ty['Name'])

myDatas = myDatas[["Name",'Add','Tel','Opentime']]

# myDatas.to_excel('data.xlsx')
#  需要安裝 openpyxl
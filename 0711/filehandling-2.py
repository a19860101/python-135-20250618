import json
#
# with open('data.json','r',encoding='utf-8') as f:
#     jsonData = f.read()
#     jsonData = json.loads(jsonData)
#
# for item in jsonData:
#     print(item['name'])
#     print(item['email'])

with open('TransService.json','r',encoding='utf-8') as f:
    jsonData = json.loads(f.read())

jsonData = [item for item in jsonData if item['animal_kind'] == '狗']

for p in jsonData:
    print(p['animal_kind'])
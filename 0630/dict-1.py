d = {
    'name': 'John',
    'mail': 'asdf@gmail.com',
    'gender': '男'
}

print(d)
print(d['name'])
print(d['mail'])
print(d['gender'])

users = [
    {
        'name': 'John',
        'mail': 'asdf@gmail.com',
        'gender': '男'
    },
    {
        'name': 'QQ',
        'mail': 'qq@GMAIL.COM',
        'gender': '女'
    }
]

# print(users[0]['name'])
for user in users:
    print(user['name'])
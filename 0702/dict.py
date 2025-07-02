d = {
    'name': 'John',
    'mail': 'asdf@gmail.com',
}

print(type(d))
print(d)
print(d['name'])

users = [
    {
        'name': 'user1',
        'mail': 'asdf@gmail.com',
        'skill': [
            {
                'name': 'html',
                'level': '3.0'
            },
            {
                'name': 'css',
                'level': '5.0'
            }
        ]
    },
    {
        'name': 'user2',
        'mail': 'xcvzv@gmail.com',
        'skill': ['photoshop','illustrator']
    }
]
print(users[1]['mail'])

print(users[0]['skill'][0]['level'])
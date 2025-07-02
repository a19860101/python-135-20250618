d = {
    'name': 'John',
    'mail': 'asdf@gmail.com',
}

# keys
# print(d.keys())
# values
# print(d.values())
# items
# print(d.items())

# for i in d.values():
#     print(i)

# for k,v in d.items():
#     print(f'{k}: {v}')


# key存在就修改，key不存在就新增
# d['name'] = 'Mary'
# d['birth'] = '1999/12/23'

# key存在就修改，key不存在就新增
# d.update({'name': 'Mary'})
# d.update({'birth': '1999/12/23'})

# key存在就維持預設，key不存在就新增
# d.setdefault('name', 'Mary')
# d.setdefault('birth', '1999/12/23')

# pop()
# d.pop('mail')

# popitem()
# d.popitem()

d.clear()
print(d)
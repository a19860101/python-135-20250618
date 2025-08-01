# 解法一
s = input()
for item in s:
    print(f'ASCII code for \'{item}\' is {ord(item)}')

r = sum([int(ord(item)) for item in s])
print(r)

# 解法二
s = input()
r = 0
for item in s:
    print(f'ASCII code for \'{item}\' is {ord(item)}')
    r += ord(item)

print(r)
# 解法三
s = input()
r = []
for item in s:
    print(f'ASCII code for \'{item}\' is {ord(item)}')
    r.append(ord(item))

print(sum(r))

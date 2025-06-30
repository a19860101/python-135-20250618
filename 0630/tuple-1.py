# tuple 元組

t = (12,52,63,32,31)
print(t)
print(t[0])
print(t[-1])
print(t[2:5])

# 使用圓括號
# 不可改變

t = list(t)
t.append(123)
t.sort()
t = tuple(t)
print(t)

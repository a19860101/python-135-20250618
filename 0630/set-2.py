s = {'apple', 'banana', 'cat'}

# 新增
s.add('kiwi')

# 移除
# 會報錯
# s.remove('qqq')

# 不報錯
# s.discard('qqq')

# 隨機移除
s.pop()

# 清除
# s.clear()

a = {'apple', 'banana', 'cat'}
b = {'apple','dog','kiwi'}

# 聯集
print(a.union(b))
print(a | b)

# 交集
print(a.intersection(b))
print(a & b)

# 差集
print(a.difference(b))
print(a - b)
print(b.difference(a))
print(b - a)

# 對稱差集
print(a.symmetric_difference(b))
print(a ^ b)

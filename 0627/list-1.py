ls1 = [1,2,3,4,5]
ls2 = [True, 'ABC', 3.14]
ls3 = list([1,2,3,4,5])

# 擷取串列
# print(ls1[2])
# print(ls1[1:4])
# print(ls1[-2])
# print(ls1[::2])

# t1 = (1,2,3,4,5)
# print(t1)
# print(type(t1))
# t1 = list(t1)
# print(t1)
# print(type(t1))
# t1 = tuple(t1)
# print(t1)
# print(type(t1))

#
# print(ls1)
# print(ls2)
# print(ls3)
#
# print(type(ls1))
# print(type(ls2))
# print(type(ls3))

# 字串->串列
s = 'hello python'
# s = list(s)
s = s.split('o')
# print(s)

# 判斷
drinks = ['紅茶','綠茶','拿鐵','奶茶']

print('拿鐵' in drinks)       # True
print('水' in drinks)        # False
print('拿鐵' not in drinks)   # False
print('水' not in drinks)    # True

if '水' not in drinks:
    print('多喝水')
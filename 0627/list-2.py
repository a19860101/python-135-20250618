drinks = ['紅茶','綠茶','拿鐵','奶茶']
coke = ['可口可樂','百事可樂']

# 常用方法

# len()
print(len(drinks))

# append() 加入資料
# drinks.append(coke)
# print(drinks)

# extend() 擴充資料
# drinks.extend(coke)
# print(drinks)

# insert() 插入資料
drinks.insert(3,'可口可樂')

# print(drinks)

# remove() 移除資料
# drinks.remove('拿鐵')
# print(drinks)

# pop() 移除最後一筆資料
# drinks.pop()
# print(drinks)

# del 移除資料
# del drinks[-1]
# print(drinks)

# clear 清空資料
drinks.clear()
print(drinks)

n = [46, 72, 15, 37, 21]
# sort() 排序
# n.sort()
# n.sort(reverse=True)
# print(n)

# reverse() 反轉
# n.reverse()

n.sort()
n.reverse()
print(n)
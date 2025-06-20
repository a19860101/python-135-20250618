# 字串方法
s = 'hello python'
# 字串長度
print(len(s))

# upper()大寫
print(s.upper())
# lower()小寫
print(s.lower())
# title()每個單字的首字大寫
print(s.title())
# capitalize()首字大寫
print(s.capitalize())

# index() 尋找該文字的索引值，找不到會報錯
print(s.index('o'))
# print(s.index('a'))

# find() 尋找該文字的索引值，找不到會回傳-1
# print(s.find('p'))
print(s.find('a'))

# count() 計算文字中出現指定文字的次數
print(s.count('o'))

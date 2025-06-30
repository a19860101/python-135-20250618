# 109
# 請撰寫一程式，讓使用者輸入一個正數s，代表正五邊形之邊長，
# 計算並輸出此正五邊形之面積（Area）。
#
# 提示1：建議使用import math模組的math.pow及math.tan
# 提示2：正五邊形面積的公式： Area = (5 * s^2)/(4 * tan(pi/5))
# 提示3：輸出浮點數到小數點後第四位。

# 輸入輸出：
# 輸入說明
# 正數s
# 輸出說明
# 正五邊形面積

# 範例輸入
# 5
# 範例輸出
# Area = 43.0119

##############################
# 304
# 請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數a，
# 利用迴圈計算從1到a之間，所有5之倍數數字總和。

# 輸入輸出：
# 輸入說明
# 一個正整數

# 輸出說明
# 所有5之倍數數字總和

# 範例輸入
# 21
# 範例輸出
# 50

# a = 21
# s = 0
print(sum([i for i in range(int(input()) + 1) if i % 5 == 0]))

# for i in range(a + 1):
#     if i % 5 == 0:
#         s += i
# print(s)

# import math

# print(math.tan(30))
# print(math.pi)
# print(math.pow(2,7))
# print(math.sqrt(2))
# print(2 ** 0.5)

n = [1,2,3,4,5]

print(sum(n))
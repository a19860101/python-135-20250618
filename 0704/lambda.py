# lambda 匿名函式
# lambda 名稱:動作

a = lambda x : x
b = lambda x : x**2
c = lambda *args: args
d = lambda price, tax=1.2 : price * tax

print(a(10))
print(b(12))
print(c(1,2,3,4,5,6))
print(d(100))
print(d(100, 1.3))

"""
lambda不需要命名
lambda只能有一行
lambda會自動回傳
"""
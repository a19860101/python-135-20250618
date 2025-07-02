# def foo(n):
#     if n == 0:
#         return 2
#     else:
#         return foo(n-1) * 2
#
# print(foo(4)) # 32
# print(foo(3)) # 16
# print(foo(2)) # 8
# print(foo(1)) # 4
# print(foo(0)) # 2

# def foo(n):
#     if n == 0:
#         return 1
#     else:
#         return n * foo(n-1)


def foo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return foo(n-1) + foo(n-2)

# print(foo(10))

for i in range(10):
    print(foo(i), end=',')
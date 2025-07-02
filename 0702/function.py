# 函式 Function
#
# def foo():
#     print('hello')
#
# def foo2(x):
#     print(x)
#
# def ntd_to_yen(dollar, exc):
#     print(dollar / exc)

# ntd_to_yen(10000, 0.205)

# def foo():
#     return 'hello'
#
# def foo2():
#     print('hello')

# 預設值
# 有預設值的參數放後面
def ntd_to_usd(dollar, exc=29):
    print(dollar / exc)

ntd_to_usd(10000)
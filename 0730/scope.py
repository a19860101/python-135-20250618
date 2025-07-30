# global variable 全域變數
# a = 'hello'
# def foo():
    # 區域變數
    # a = 100

a = ''
def test():
    global a
    a = 'hello'

test()

print(a)


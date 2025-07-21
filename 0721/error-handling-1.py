# x = 'hello'
try:
    print(x)
except NameError as e:
    print(e)
except:
    print('error')
else:
    print('else')
finally:
    print('Complete')

i = -10
# if i < 0:
#     raise Exception('請輸入正整數')

# if i>0:
#     print('ok')
# else:
#     raise Exception('請輸入正整數')

# Built in Exceptions
# https://docs.python.org/3/library/exceptions.html
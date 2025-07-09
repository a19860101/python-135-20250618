# import datetime as dt


# import datetime
# print(datetime.datetime.now())

from datetime import datetime
# print(datetime.now())

# 模組.方法

# from 模組 import 方法

now = datetime.now()
print(now)
print(now.date())
print(now.time())

print(now.weekday())
print(now.isoweekday())
print(now.isoformat())
print(now.isocalendar())

print(now.ctime())

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

from datetime import date

q = date.today()
print(q)
print(q.year)
print(q.month)
print(q.day)

from datetime import time


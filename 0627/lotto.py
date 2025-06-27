# 大樂透電腦選號
# 1-49 6

import random

# print(random.randrange(1,9))
# print(random.randint(1,9))

result = []

while len(result) < 7:
    n = random.randint(1,49)
    if n not in result:
        result.append(n)

# print(result)

# print(f'大樂透隨機選號結果為:{result}')
print(result)

r =  ','.join(str(i) for i in result[:-1])

print(f'大樂透隨機選號結果:{r}特別號{result[-1]}')

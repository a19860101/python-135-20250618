import random

a = 1
b = 100
ans = random.randint(a, b)
print(ans)

ip = int(input(f'請猜數字{a}-{b}之間:'))

while ans != ip:
    if ip > ans:
        b = ip
        print('太大')
        print(f'{a}以上{b}以下')
    else:
        a = ip
        print('太小')
        print(f'{a}以上{b}以下')

    ip = int(input(f'請猜數字{a}-{b}之間:'))
print('Bingo!!!!')


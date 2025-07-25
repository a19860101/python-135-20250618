n = int(input())
for i in range(n):
    s = input()
    r = sum([int(item) for item in list(s)])
    print(f'Sum of all digits of {s} is {r}')
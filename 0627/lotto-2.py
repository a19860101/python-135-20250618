import random
#
result = random.sample(range(1,50),7)

print(result)

r =  ','.join(str(i) for i in result[:-1])

print(f'大樂透隨機選號結果:{r}特別號{result[-1]}')

result = random.sample(['apple','banana','cat'],2)

print(result)


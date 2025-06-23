# s1 = 'hello {}'
# s1 = s1.format('john')
# print(s1)
#
# s2 = 'hello {} , 今天氣溫為 {} 度C'
# s2 = s2.format('John',33)
# print(s2)
#
# s3 = 'hello {1} , 今天氣溫為 {0} 度C'
# s3 = s3.format(33, 'John')
# print(s3)
#
# s4 = 'hello {name} , 今天氣溫為 {temp} 度C'
# s4 = s4.format(temp='33', name='Max')
# print(s4)

# s = 'hello {:*^10.1s} , 今天氣溫為 {:10.2f} 度C'
# s = s.format('John', 28.53)
s = 'hello {name:*^10.1s} , 今天氣溫為 {temp:10.2f} 度C'
s = s.format(temp=33.45, name='Max')
print(s)

# print('{:x}'.format(255))
r = 128
g = 12
b = 255

# rgb(128 , 12, 255)
print('{:02x}{:02x}{:02x}'.format(r,g,b))
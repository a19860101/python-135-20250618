# poker = []
# for i in range(5):
#     p = input()
#
#     if p == 'A':
#         poker.append(1)
#     elif p == 'K':
#         poker.append(13)
#     elif p == 'Q':
#         poker.append(12)
#     elif p == 'J':
#         poker.append(11)
#     else:
#         poker.append(int(p))
#
# print(sum(poker))

poker = 0
for i in range(5):
    p = input()
    if p == 'A':
        poker+=1
    elif p == 'K':
        poker+=13
    elif p == 'Q':
        poker+=12
    elif p == 'J':
        poker+=11
    else:
        poker+=int(p)
print(poker)

# r = 0
# for i in range(5):
#     r += i
# print(r)
#
# q = [0,1,2,3,4]
#
# print(sum(q))
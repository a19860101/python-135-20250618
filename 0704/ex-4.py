import random
user1 = input('請出拳(0石頭 5布 2剪頭)')
user2 = random.sample(['0','5','2'],1)
# 5,2
def game(u1, u2):
    win = {'0':'2', '2':'5', '5':'0'}

    if win[u1] == u2:
        print(u1, u2)
        return 'You won'

    if win[u2] == u1:
        print(u1, u2)
        return 'You lose'

    print(u1, u2)
    return 'Draw'

print(game(user1, user2[0]))
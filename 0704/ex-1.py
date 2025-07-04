#
def jp_tw(mode,dollar,exc=0.20):
    if mode == '1':
        # print(dollar / exc)
        print(f'{dollar}台幣約為{dollar / exc}日幣')
    else:
        # print(dollar * exc)
        print(f'{dollar}日幣約為{dollar * exc}台幣')


def main():
    m = input('台幣轉日幣請按1,日幣轉台幣請按2:')
    d = float(input('請輸入金額:'))
    jp_tw(m, d, 0.212)

# jp_tw(m, d, 0.212)


main()
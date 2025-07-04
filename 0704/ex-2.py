def tw_us(dollar,exc=28.9):
    return dollar // exc

def tw_jp(dollar, exc=0.205):
    return dollar // exc

def us_tw(dollar, exc=28.9):
    return dollar * exc

def jp_tw(dollar, exc=0.205):
    return dollar * exc


def main():
    while True:
        m = input('台幣轉日幣請按 0\n台幣轉美金請按 1\n日幣轉台幣請按 2\n美金轉台幣請按 3\n結束請按9\n')
        if m == '9':
            print('程式結束')
            return
        d = float(input('請輸入金額:'))

        match m:
            case '0':
                print(tw_jp(d))
            case '1':
                print(tw_us(d))
            case '2':
                print(jp_tw(d))
            case '3':
                print(us_tw(d))



main()
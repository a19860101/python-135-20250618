class Test:
    def __init__(self, exc=0.20):
        self.mode = input('台幣轉日幣請按1,日幣轉台幣請按2:')
        self.dollar = float(input('請輸入金額:'))
        self.exc = exc

    def jp_tw(self):
        if self.mode == '1':
            return f'{self.dollar}台幣約為{self.dollar / self.exc}日幣'
        else:
            # print(dollar * exc)
            return f'{self.dollar}日幣約為{self.dollar * self.exc}台幣'

    def main(self):
        return self.jp_tw()

x = Test()
print(x.main())

class Test:
    def __init__(self,x):
        self.x = x


    def q1(self):
        return self.x

    def q2(self):
        return self.q1()

    def q3(self):
        return self.q2()


x = Test(123)

print(x.q2())
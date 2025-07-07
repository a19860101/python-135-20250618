class Role:
    def __init__(self):
        self.name = '廟窪塚子'
        self.attr = ['草','毒']
        self.weak = ['火']

    # @property
    @staticmethod
    def test():
        return 'hello'


class Seed(Role):
    def __init__(self):
        super().__init__()
        self.name = 'hello'

    # @staticmethod
    # def test():
    #     return '123'

x = Seed()
print(x.name)
print(x.attr)
print(x.weak)
# x.test = 'qqq'
# print(x.test)
print(x.test())

# @property 唯讀
# @staticmethod 靜態方法
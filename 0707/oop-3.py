class Role:
    def __init__(self, name, attr, weak):
        self.name = name
        self.attr = attr
        self.weak = weak

class Seed(Role):
    def speak(self, s):
        return f'{self.name}:{s}'

class Mouse(Role):
    def speak(self, s):
        return f'{self.name}:{s}'

x = Seed('廟窪塚子',['草','毒'],['火'])
print(x.name)
print(x.speak('種子種子種子種子種子'))

y = Mouse('匹咖邱',['電'], ['沒有弱點'])
print(y.name)
print(y.speak('批卡批卡'))
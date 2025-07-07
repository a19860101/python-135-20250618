class Role:
    def __init__(self, name, attr, weak):
        self.name = name
        self.attr = attr
        self.weak = weak

    def speak(self, s):
        return f'{self.name}:{s}'

r1 = Role('廟窪塚子',['草','毒'],['火'])

print(r1.name)
print(r1.attr)
print(r1.weak)

print(r1.speak('種子種子種子種子種子'))

r2 = Role('匹咖邱',['電'], ['沒有弱點'])
print(r2.name)
print(r2.attr)
print(r2.weak)
print(r2.speak('批卡批卡'))



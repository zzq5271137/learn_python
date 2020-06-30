"""
面向对象简介
"""


class Person(object):
    def __init__(self, name, age, style):
        self.name = name
        self.age = age
        self.style = style

    def eat(self):
        print(u'我是%s, 我吃饭比较%s' % (self.name, self.style))


p1 = Person('张三', 18, '文静')
p1.eat()
p2 = Person('李四', 28, '狂野')
p2.eat()

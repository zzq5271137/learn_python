"""
动态删除属性
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('zzq', 27)
del p1.name
delattr(p1, 'age')

"""
__class__
"""

"""
__class__可以拿到当前对象所属的类的引用(注意, 拿到的不是当前对象所属的类的类名, 而是所属的类的引用)
"""


class Person(object):
    def __init__(self, name):
        self.name = name


p1 = Person('zzq1')
print(p1.__class__)
print(Person)

p2 = p1.__class__('zzq2')  # __class__可以创建对象
print(p2.name)

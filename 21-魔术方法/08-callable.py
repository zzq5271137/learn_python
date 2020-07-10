"""
可调用的对象的魔术方法
"""

"""
可调用的对象的魔术方法:
在Python中, 一个特殊的魔术方法可以让类实例的行为表现得像函数一样, 你可以调用他们, 可以将它作为参数传递到另一个函数里进行调用等等;
这个魔术方法是, __call__(self, [args...]), 它允许一个类的实例像函数一样被调用; 从实质上说,
my_obj()和my_obj.__call__()是一样的; 注意, __call__的参数是可变的, 这意味着你可以定义__call__为你想要的函数,
无论它有多少个参数;
"""


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)

    def __call__(self, x, y):
        self.x, self.y = x, y


print(callable(Coordinate))  # callable()可以判断一个类或对象是否是可调用的
c1 = Coordinate(1, 3)
print(callable(c1))
print(c1)
c1(2, 4)
print(c1)

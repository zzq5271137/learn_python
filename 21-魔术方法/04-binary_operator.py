"""
二元运算符魔术方法
"""

"""
二元运算符魔术方法:
1. __add__(self, other)魔术方法:
   相加, 在两个对象之间使用"+"的时候自动调用的方法, 返回一个对象;
2. __sub__(self, other)魔术方法:
   相减, 在两个对象之间使用"-"的时候自动调用的方法, 返回一个对象;
3. __mul__(self, other)魔术方法:
   相乘, 在两个对象之间使用"*"的时候自动调用的方法, 返回一个对象;
4. __div__(self, other)魔术方法:
   相除, 在两个对象之间使用"/"的时候自动调用的方法, 返回一个对象;
   在Python2中生效;
5. __floordiv__(self, other)魔术方法:
   整除, 在两个对象之间使用"//"的时候自动调用的方法, 返回一个对象;
6. __truediv__(self, other)魔术方法:
   真除, 在两个对象之间使用"/"的时候自动调用的方法, 返回一个对象;
   在Python3中使用"/"会执行这个方法; 在Python2中, 默认使用__div__方法, 
   如果使用"from __future__ import division", 那么就会使用__truediv__方法;
7. __mod__(self, other)魔术方法:
   取模, 在两个对象之间使用"%"的时候自动调用的方法, 返回一个对象;
"""


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Coordinate(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Coordinate(x, y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Coordinate(x, y)

    def __floordiv__(self, other):
        x = self.x // other.x
        y = self.y // other.y
        return Coordinate(x, y)

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        return Coordinate(x, y)

    def __mod__(self, other):
        x = self.x % other.x
        y = self.y % other.y
        return Coordinate(x, y)


c1 = Coordinate(3, 4)
c2 = Coordinate(2, 2)
print("c1: %s, c2: %s" % (c1, c2))
print("c1 + c2: %s" % (c1 + c2))
print("c1 - c2: %s" % (c1 - c2))
print("c1 * c2: %s" % (c1 * c2))
print("c1 // c2: %s" % (c1 // c2))
print("c1 / c2: %s" % (c1 / c2))
print("c1 % c2: {}".format(c1 % c2))

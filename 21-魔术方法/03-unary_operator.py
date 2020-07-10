"""
一元运算符魔术方法
"""

"""
一元运算符魔术方法:
1. __pos__(self)魔术方法:
   取正, 在这个对象前面使用正号("+")时自动调用的方法, 返回一个对象;
2. __neg__(self)魔术方法:
   取反, 在这个对象前面使用负号("-")时自动调用的方法, 返回一个对象;
3. __abs__(self)魔术方法:
   取绝对值, 在这个对象上使用abs()函数时自动调用的方法, 返回一个对象;
4. __invert__(self)魔术方法:
   位运算逐位取反, 在这个对象前使用"~"时自动调用的方法, 返回一个对象;
   ("~"操作符在Python中是位操作符, 表示逐位取反)
"""


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)

    def __pos__(self):
        return self

    def __neg__(self):
        return Coordinate(-self.x, -self.y)

    def __abs__(self):
        return Coordinate(abs(self.x), abs(-self.y))

    def __invert__(self):
        return Coordinate(255 - self.x, 255 - -self.y)  # 瞎写的, 没意义, 并不是位操作中的逐位取反操作


my_coordinate = Coordinate(3, -4)
print(my_coordinate)
print('+my_coordinate: %s' % +my_coordinate)
print('-my_coordinate: %s' % -my_coordinate)
print('abs(my_coordinate): %s' % abs(my_coordinate))
print('~my_coordinate: %s' % ~my_coordinate)

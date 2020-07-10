"""
增量赋值魔术方法
"""

"""
增量赋值魔术方法:
1. __iadd__魔术方法:
   在给对象做"+="运算时会自动执行的方法, 返回一个对象;
2. __isub__魔术方法:
   在给对象做"-="运算时会自动执行的方法, 返回一个对象;
3. __imul__魔术方法:
   在给对象做"*="运算时会自动执行的方法, 返回一个对象;
4. __ifloordiv__魔术方法:
   在给对象做"//="运算时会自动执行的方法, 返回一个对象;
5. __itruediv__魔术方法:
   在给对象做"/="运算时会自动执行的方法, 返回一个对象;
6. __imod__魔术方法:
   在给对象做"%="运算时会自动执行的方法, 返回一个对象;
"""


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)

    def __iadd__(self, other):
        return Coordinate(self.x + other, self.y + other)

    def __isub__(self, other):
        return Coordinate(self.x - other, self.y - other)

    def __imul__(self, other):
        return Coordinate(self.x * other, self.y * other)

    def __ifloordiv__(self, other):
        return Coordinate(self.x // other, self.y // other)

    def __itruediv__(self, other):
        return Coordinate(self.x / other, self.y / other)

    def __imod__(self, other):
        return Coordinate(self.x % other, self.y % other)


my_coordinate = Coordinate(3, 5)
print(my_coordinate)
my_coordinate += 2
print('my_coordinate += 2: %s' % my_coordinate)
my_coordinate = Coordinate(3, 5)
my_coordinate -= 2
print('my_coordinate -= 2: %s' % my_coordinate)
my_coordinate = Coordinate(3, 5)
my_coordinate *= 2
print('my_coordinate *= 2: %s' % my_coordinate)
my_coordinate = Coordinate(3, 5)
my_coordinate /= 2
print('my_coordinate /= 2: %s' % my_coordinate)
my_coordinate = Coordinate(3, 5)
my_coordinate //= 2
print('my_coordinate //= 2: %s' % my_coordinate)
my_coordinate = Coordinate(3, 5)
my_coordinate %= 2
print('my_coordinate %= 2: {}'.format(my_coordinate))

"""
__slots__魔术变量
"""

"""
前面讲到, 我们可以动态地给类/对象添加属性和方法; 但有的时候, 我们想指定我们的类/对象只能使用我指定的这些属性,
那么这时候就可以使用__slots__魔术变量; 这个变量是一个列表或者元组, 里面存放属性的名字;
然后在外面使用时, 就只能添加这个魔术变量中指定的属性, 不能添加其他属性;
__slots__这个变量, 只能在新式类中去使用, 不能在旧式类中使用;
"""


class Person(object):
    __slots__ = ['name', 'age']  # 也可以使用元组

    def __init__(self, name):
        self.name = name


p1 = Person('zzq')
setattr(p1, 'age', 27)
print(p1.age)

try:
    setattr(p1, 'studentid', '820064')
    print(p1.studentid)
except AttributeError as err:
    print(err)

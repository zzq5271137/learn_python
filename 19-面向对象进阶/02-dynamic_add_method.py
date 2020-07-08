"""
动态添加方法
"""

import types

"""
动态添加实例方法:
意思是方法不是在类定义的时候添加的, 而是创建完这个对象后, 在程序运行过程中添加的;
如果想要在运行的时候添加方法, 就应该用到types.MethodType()这个函数了;
"""


class Person1(object):
    def __init__(self, name):
        self.name = name


def run(self, duration):
    print("%s在奔跑, 需要跑%d小时" % (self.name, duration))


# types.MethodType()的第一个参数是这个函数本身, 第二个参数是在调用run()这个函数的时候, 传给它的第一个参数,
# 这里动态添加的是实例方法, 所以方法的第一个参数是self, 所以就把p1传进去就行了;
p1 = Person1('zzq')
p1.run = types.MethodType(run, p1)
p1.run(3)

print("####################################################")

"""
动态添加类方法:
是把这个方法添加给类, 因此动态添加类方法时不是给对象添加, 而是给类添加; 并且不需要使用types.MethodType(),
直接将这个函数赋值给类就行了, 但是需要使用classmethod装饰器, 将这个方法设置为一个类方法;
"""


class Person2(object):
    country = '中国'

    def __init__(self, name):
        self.name = name


@classmethod
def run(cls):
    print("%s在奔跑" % cls.country)


Person2.run = run
Person2.run()

print("####################################################")

"""
动态添加静态方法:
是把这个方法添加给类, 因此也是直接给类添加的, 并且要使用staticmethod装个装饰器;
"""


class Person3(object):
    country = '中国'

    def __init__(self, name):
        self.name = name


@staticmethod
def run():
    print("在奔跑")


Person3.run = run
Person3.run()

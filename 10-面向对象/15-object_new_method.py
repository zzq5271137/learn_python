"""
__new__()方法
"""

"""
创建一个对象, 先会调用__new__()方法, 当对象创建好后, 再调用__init__()方法去做初始化 
"""


class Person(object):
    # __new__()方法是在对象被创建之前自动执行的, 会返回一个当前类的对象
    def __new__(cls, *args, **kwargs):  # __new__()方法属于类方法
        print("Person __new__()")
        return super().__new__(cls, *args, **kwargs)  # 如果重写了__new__()方法, 最后一定要返回当前这个类的对象

    # __init__()方法是在对象被创建完毕之后被立刻自动执行的, 这里的创建完毕指的是分配好了对象的内存空间
    def __init__(self):
        print("Person __init__()")


p1 = Person()
print(p1)

"""
单例模式
"""

"""
单例设计模式是指, 某个类或者模型在整个程序运行期间只存在一份实例对象;
"""


class Calculator(object):
    __instance = None

    def __new__(cls, *args, **kwargs):  # 通过__new__()方法来实现单例模型
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        self.name = name


c1 = Calculator('c1')
print("id: {}, name: {}".format(id(c1), c1.name))  # id()函数返回对象的唯一标识符, 标识符是一个整数
c2 = Calculator('c2')
print("id: {}, name: {}".format(id(c2), c2.name))

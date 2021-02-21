"""
单例模式
"""

"""
单例设计模式是指, 某个类或者模型在整个程序运行期间只存在一份实例对象;
"""


class Calculator(object):
    __instance = None

    # 这种写法的单例模式是线程不安全的; 如果想要线程安全的单例模式, 需要使用锁(之后会讲到);
    def __new__(cls, *args, **kwargs):  # 通过__new__()方法来实现单例模型
        if not cls.__instance:
            # cls.__instance = super().__new__(cls)  # 简写
            cls.__instance = super(Calculator, cls).__new__(cls)
        return cls.__instance

    def __init__(self, name, age):
        self.name = name
        self.age = age


c1 = Calculator(name='c1', age=101)
print("create c1: Calculator(name='c1', age=101)")
print(f"c1: id={id(c1)}, name={c1.name}, age={c1.age}")  # id()函数返回对象的唯一标识符, 标识符是一个整数
c2 = Calculator(name='c2', age=102)
print("create c2: Calculator(name='c2', age=102)")
print(f"c2: id={id(c2)}, name={c2.name}, age={c2.age}")
print(f"c1: id={id(c1)}, name={c1.name}, age={c1.age}")

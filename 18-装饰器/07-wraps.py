"""
wraps装饰器
"""


def greet(func):
    def wrapper(*args, **kwargs):
        print('func start execute')
        func(*args, **kwargs)
        print('func end execute')

    return wrapper


@greet
def add(x, y):
    print('%d + %d = %d' % (x, y, x + y))


def minus(x, y):
    print('%d - %d = %d' % (x, y, x - y))


# 在Python中, 所有东西都是对象, 函数也不例外
# 函数有一个__name__属性, 这个属性记录了该函数的名字;
# 观察不加@greet装饰器和加上@greet装饰器后, __name__值的不同
print(add.__name__)
print(minus.__name__)

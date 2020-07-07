"""
wraps装饰器
"""

from functools import wraps


def greet(func):
    def wrapper(*args, **kwargs):
        print('func start execute')
        func(*args, **kwargs)
        print('func end execute')

    return wrapper


"""
下面的代码, 在add()函数上加上@greet装饰器, 等价于以下这种写法:
    def add(x, y):
        print('%d + %d = %d' % (x, y, x + y))
    add = greet(add)
而greet()函数返回一个wrapper()函数, 即add实际指向的是greet()返回的wrapper()函数,
所以打印add.__name__的值为wrapper
"""


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

print("#############################################################")

"""
以上的现象, 其实会造成一些问题, 因为有时候我们可能需要获取某函数的名字, 但如果加上装饰器该函数的名字就会改变的话,
就会造成问题; 所以需要使用wraps装饰器, 使得即使函数使用装饰器, 但是它的__name__属性的值依然保持原来的那个值;
"""


def greet2(func):
    @wraps(func)  # @wraps装饰器的使用, 把它加包裹住func()真正运行的位置的函数的顶部(以后要养成习惯, 自定义装饰器的时候一定要加@wraps装饰器)
    def wrapper(*args, **kwargs):
        print('func start execute')
        func(*args, **kwargs)
        print('func end execute')

    return wrapper


@greet2
def multiple(x, y):
    print('%d * %d = %d' % (x, y, x * y))


print(multiple.__name__)

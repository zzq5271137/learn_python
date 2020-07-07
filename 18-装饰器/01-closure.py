"""
闭包(closure)
"""

"""
什么是闭包:
如果在一个函数中, 定义了另外一个函数, 并且里面函数使用了外面函数的变量, 并且外面函数返回了里面函数的引用,
那么称里面的这个函数为闭包; 例如下面的小例子;
"""


def greet(name):
    def say_hello():  # 这个函数就称为闭包
        print('hello, my name is %s' % name)

    return say_hello  # 返回闭包时没有加圆括号, 代表着把这个函数的引用返回回去, 而不是执行完这个函数之后把结果返回回去


say_hello_res = greet('zzq')  # greet()函数返回的是它内部的say_hello()函数的引用
print(say_hello_res)
print(type(say_hello_res))  # function
say_hello_res()  # 可以直接调用

# 简化写法
greet('zzq2')()  # 牢记这种写法

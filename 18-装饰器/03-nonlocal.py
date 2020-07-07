"""
nonlocal关键字
"""

"""
如果想要在闭包中修改外面函数的变量, 就可以使用nonlocal关键字;
(nonlocal关键字的作用与global关键字有点相似, 记得, global关键字的作用是, 如果函数内想要修改全局变量的值,
可以使用global关键字, 即, global关键字引用的是全局变量, nonlocal关键字引用的是外层函数内的局部变量)
"""


def greet(name):
    def say_hello():
        nonlocal name
        name = 'helllo %s' % name
        print(name)

    return say_hello


greet('zzq')()

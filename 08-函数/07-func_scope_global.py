"""
global关键字
"""

name = 'zzq'


def greet():
    global name  # 想要在函数体内修改全局变量的值, 就必须在修改前, 先将该变量使用global关键字声明一下
    name = 'zzq_new'
    print('hello, %s' % name)


greet()

print(name)

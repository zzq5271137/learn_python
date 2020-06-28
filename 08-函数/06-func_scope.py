"""
变量的作用域
"""

greetstr = 'hello'  # 这个greetstr变量就是全局变量, 在这个.py文件中的任何地方都可以使用


def greet():
    name = 'zzq'  # 这个name变量是局部变量/本地变量, 只能在这个函数体内部使用, 无法在函数体外被使用
    print("%s, %s" % (greetstr, name))  # 在函数体内依然可以使用greetstr全局变量


greet()


def greet2():
    greetstr = 'good night'  # 这个就是全局变量的覆盖, 即本地创建了一个和全局变量名称相同的变量
    name = 'zzq'
    print("%s, %s" % (greetstr, name))  # 在使用变量时, 会先在本地(方法体内)查找有没有, 有就直接使用, 没有就再往上一层去寻找


greet2()

"""
循环引用
"""

"""
这里就出现了循环引用的问题(因为这里导入的是模块里的具体方法);
还是跟sys.modules以及导入模块时执行的那3步有关(注意观察执行此处代码时的具体报错信息, 参照那3步, 自行分析)

注: 如果以后开发时发现, 你的导入路径都是对的, 但是就是无法导入, 可能就是发生了循环导入的问题;

如何解决这个问题呢? 这个问题并不是Python本身的问题, 归根结底这是你程序结构设计的问题, 
应该尽量避免两个模块的相互引用, 或者尽量避免模块的导入链条形成一个环形;
"""

from loop_reference_2.loop_b import sayhello_b

print("loop_a been referenced")


def sayhello_a():
    print("hello loop_a")

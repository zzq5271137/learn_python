"""
如果是在模块中写了这个变量, 它将控制"from 模块名 import *"的行为;
如果不在模块中定义__all__变量, 那么"from 模块名 import *"将默认导入该模块下的所有东西;
"""
__all__ = ['GLOBAL_ZZQ']

GLOBAL_ZZQ = 'zzq'


def sayhello():
    print("hello world")


class Person(object):
    def __init__(self):
        print('Person init')

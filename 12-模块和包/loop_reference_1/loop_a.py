"""
循环引用
"""

"""
记得导入模块时会执行的3步(详见05-import_principle.py), 由于有sys.modules的存在, 所以不会重复导入模块,
也就不会重复执行导入的模块的代码, 并且这里导入的是整个模块(而不是模块内的具体类、方法), 所以这里不会出现循环引用的问题;
"""

from loop_reference_1 import loop_b

print("loop_a been referenced")


def sayhello_a():
    print("hello loop_a")

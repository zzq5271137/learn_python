"""
可迭代的对象(Iterable)
"""

from collections import Iterable

"""
什么是可迭代的对象(Iterable对象):
可以直接使用for循环遍历的对象, 称为可迭代的对象; 常见的可迭代的对象有: list、tuple、dict、set、str、文件指针对象以及生成器;
更加准确地判断一个对象是否是可迭代的对象的方法是, 这个对象有一个__iter__()方法, 并且这个方法会返回一个迭代器对象,
这种对象就叫做可迭代的对象; 
注意, 可迭代的对象和迭代器对象是两个概念, 不要混为一谈;
代码中, 可以使用isinstance()方法判断一个对象是否是Iterable对象(Iterable是一个类)
"""

# 判断一个对象是否是可迭代的对象: 可以使用isinstance()方法判断一个对象是否是Iterable对象(Iterable是一个类)
# 注: isinstance()方法用来判断某一个对象是不是属于某一个类
temp = [1, 2, 3]
print('%s is Iterable: %s' % (type(temp), isinstance(temp, Iterable)))  # 列表是一个可迭代对象
temp = 'zzq'
print('%s is Iterable: %s' % (type(temp), isinstance(temp, Iterable)))  # 字符串是一个可迭代对象
temp = ('zzq', 27, '820064')
print('%s is Iterable: %s' % (type(temp), isinstance(temp, Iterable)))  # 元组是一个可迭代对象
temp = {'name': 'zzq', 'age': 27, 'id': '820064'}
print('%s is Iterable: %s' % (type(temp), isinstance(temp, Iterable)))  # 字典是一个可迭代对象
temp = range(1, 10)
print('%s is Iterable: %s' % (type(temp), isinstance(temp, Iterable)))  # range类是一个可迭代对象
temp = 27
print('%s is Iterable: %s' % (type(temp), isinstance(temp, Iterable)))  # 整型不是一个可迭代对象


# 自己的类如果实现了__iter__()方法, 则也是Iterable的
class MyRange(object):
    def __iter__(self):
        pass


temp = MyRange()
print('%s is Iterable: %s' % (type(temp), isinstance(temp, Iterable)))

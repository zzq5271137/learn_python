"""
Python的垃圾回收机制: 引用计数
"""

import sys

"""
引用计数:
在Python中使用了引用计数这一技术来实现内存管理; 一个对象被创建完成后就有一个变量指向它, 此时它的引用计数为1,
以后如果有其他变量指向它, 引用计数也会相应增加; 如果一个变量不再指向这个对象, 那么这个对象的引用计数减1;
如果一个对象没有任何变量指向它, 也即引用计数为0, 那么这个对象就会被Python回收;
可以使用sys.getrefcount()来获取一个对象的引用计数;

(Python和Java一样, 都是自动的垃圾回收)
"""


class Person(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):  # 析构函数, 我们经常在析构函数中做一些收尾工作, 比如流的关闭操作(例如文件的close())
        print("%s: 析构函数被调用了" % self.name)


p1 = Person('zzq1')
print(sys.getrefcount(p1))  # 这里会打印出2, 因为sys.getrefcount()函数中有一个变量引用到这个对象了, 加上p1, 所以是两个
p2 = p1
print(sys.getrefcount(p1))
del p1
del p2

"""
循环引用
"""

"""
引用计数这一技术虽然可以在一定程度上解决内存管理的问题, 但是还是有不能解决的问题, 即循环引用;
比如现在分别有两个对象分别为a和b, a指向了b, b又指向了a, 那么他们两个的引用计数永远都不会为0;
这就造成了内存泄漏的问题(所谓内存泄漏, 指的是某一块内存空间没有被释放, 但是我们程序中再也拿不到了);
"""


class Person(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("%s执行了del函数" % self.name)


while True:
    p1 = Person('p1')
    p2 = Person('p2')
    p1.next = p2
    p2.prev = p1
    del p1
    del p2
    a = input('test: ')

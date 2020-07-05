"""
自定义可迭代的对象和迭代器对象
"""


class MyRangeIterator(object):
    """
    自定义的迭代器对象
    """

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            temp = self.current
            self.current += 1
            return temp
        else:
            raise StopIteration()


class MyRange(object):
    """
    自定义的一个类似于range的类(自定义的可迭代的对象)
    """

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        """
        这里的__iter__()方法需要返回一个迭代器对象
        """
        return MyRangeIterator(self.start, self.end)


"""
for循环的原理:
当执行"for x in Iterable对象"时, 会通过该Iterable对象的__iter__()方法拿到迭代器对象,
拿到迭代器对象后, 在每次循环中, 会调用该迭代器对象的__next__()方法去获取值, 并赋值给x, 
然后你就可以在循环体内使用x了; 当调用__next__()方法抛出StopIteration异常时, 会退出循环;
"""
for x in MyRange(1, 11):
    print(x, end=' ')
print()

print("###########################################")

"""
使用while循环模拟for...in...底层是实现原理;
获取my_range的迭代器有两种方式, 一种是直接通过my_range的__iter__()方法(不推荐), 另一种是通过iter()函数;
"""
my_range = MyRange(1, 11)
my_iterator = iter(my_range)
while True:
    try:
        x = my_iterator.__next__()
        print(x, end=' ')
    except StopIteration:
        break

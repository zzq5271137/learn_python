"""
自定义可迭代的对象和迭代器对象
"""

"""
在03-my_iterable_iterator_1.py中, 我们自己实现了一个可迭代对象, 里面的__iter__()方法,
返回了一个我们自己实现的另一个迭代器对象; 
其实, 大可不必分成两个类来实现, 可以让同一个对象拥有两种身份(既是可迭代对象又是迭代器对象);
"""


class MyRange(object):
    """
    自定义的一个类似于range的类(自定义的可迭代的对象和迭代器对象)
    """

    def __init__(self, start, end):
        self.start = start
        self.current = start
        self.end = end

    def __iter__(self):
        """
        这里的__iter__()方法需要返回一个迭代器对象;
        由于本类既是可迭代对象又是迭代器对象, 所以返会自身即可;
        """
        return self

    def __next__(self):
        if self.current < self.end:
            temp = self.current
            self.current += 1
            return temp
        else:
            """
            但是以这种方式实现的MyRange, 如果想要被多次遍历, 这里的代码必须做出改变;
            即, 当在一次遍历中遍历到末尾时, 在抛出StopIteration异常之前, 需要重置self.current的值;
            因为如果不重置self.current的值, 当在下一次遍历该对象时, 因为是同一个对象, 
            所以self.current的值还保留在上一次遍历时的值(即最大值), 所以会直接抛出StopIteration异常, 退出循环;
            而在03-my_iterable_iterator_1.py中的写法就不会出现这个问题, 因为每次遍历MyRange对象,
            在调用它的__iter__()方法时, 它都是返回一个新的MyRangeIterator对象;
            """
            self.current = self.start
            raise StopIteration()


my_range = MyRange(1, 11)

# 第一次遍历
print("第一次遍历my_range")
for x in my_range:
    print(x, end=' ')
print()

print("###########################################")

# 第二次遍历
print("第二次遍历my_range")
for y in my_range:
    print(y, end=' ')
print()

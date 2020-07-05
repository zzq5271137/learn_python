"""
迭代器对象(Iterator)
"""

from collections import Iterable, Iterator

"""
什么是迭代器对象:
迭代器对象可以让我们访问/遍历集合的时候变得非常方便; 之前我们通过for...in...的方式访问/遍历一个集合的时候, 
底层就是使用迭代器对象来完成的; 如果没有迭代器对象, 那么我们就只能通过while循环, 每次循环的时候通过下标来访问了;

在01-Iterable.py的最后, 我们创建了一个自己的类并实现了__iter__()方法, 使之成为了一个可迭代对象;
但是如果仅仅是这样(__iter()__方法体仅仅是"pass"), 这个类的实例并不能被for...in...的方式进行遍历; 
想要使用for...in...进行遍历, 还需要迭代器对象; 
即, 需要Iterable(即__iter__()方法)和Iterator(即__next__()方法和__iter__()方法)结合, 才可以使用for循环进行遍历,
即, 一个对象能够被for循环遍历的条件是它是一个Iterable对象, 但是能真正遍历出值的条件是它的__iter__()方法返回了一个Iterator对象,
如果它的__iter__()方法没有返回一个Iterator对象, 当使用for循环进行遍历时, 会抛出异常:
"TypeError: iter() returned non-iterator of type 'NoneType'";
迭代器对象的实现:
1. 在Python2中, 实现了__iter__()方法和next()方法, 并且在next()方法中返回了值的对象, 叫做迭代器对象;
2. 在Python3中, 实现了__iter__()方法和__next__()方法, 并且在__next__()方法中返回了值的对象, 叫做迭代器对象;
3. 如果迭代器对象没有值可返回了, 那么应该在next()或者__next__()方法中抛出一个StopIteration异常;
即, 可以通过一个对象是否有一个以上面的方式实现的__iter__()方法和__next__()方法来判断一个对象是否是迭代器对象(Iterator对象);
(只有__next__()方法和__iter__()方法都实现, 才是Iterator对象, 如果只实现了__iter__()方法, 则只是Iterable对象,
如果只实现了__next__()方法, 则既不是Iterable对象也不是Iterator对象)
注意, 迭代器对象和可迭代的对象是两个概念, 不要混为一谈;
代码中, 可以使用isinstance()方法判断一个对象是否是Iterator对象(Iterator是一个类)
"""


# 判断一个对象是迭代器对象: 可以使用isinstance()方法判断一个对象是否是Iterator对象(Iterator是一个类)
# 注: isinstance()方法用来判断某一个对象是不是属于某一个类
class MyRange(object):
    def __iter__(self):
        pass

    def __next__(self):
        pass


temp = MyRange()
print('%s is Iterable: %s' % (type(temp), isinstance(temp, Iterable)))
print('%s is Iterator: %s' % (type(temp), isinstance(temp, Iterator)))

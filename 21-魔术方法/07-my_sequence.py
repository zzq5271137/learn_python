"""
自定义序列的魔术方法
"""

"""
序列:
在Python中内置了一些数据类型, 比如列表、元组、字典等; 这些数据类型之所以能够表现出一些序列的行为,
例如下标操作、遍历等等, 是因为他们都实现了一些协议, 或者一些魔术方法; 如果我们自己写一个类,
也实现这些协议或者魔术方法, 其实我们也可以定义属于自己的序列;

一些序列容器的魔术方法:
1. __len__(self):
   在使用len(obj)函数时会调用这个方法;
2. __getitem__(self, key):
   在使用下标操作时, 例如temp['key'], 以及切片操作时会调用这个方法;
3. __setitem__(self, key, value):
   在给这个容器设置key和value时会调用这个方法;
4. __delitem__(self, key):
   在删除容器中的某个key对应的这个值时会调用这个方法;
5. __iter__(self):
   在遍历这个容器的时候会调用这个方法, 然后返回一个迭代器对象, 再调用迭代器对象的__next__方法,
   可以把这个容器中的所有值遍历出来; 详见: 16-迭代器
6. __reversed__(self):
   在调用reversed(obj)函数时会调用这个方法;
   
以下示例将上面的这些魔术方法总结起来, 写一个自定义的容器, 并且能够实现head、tail、last、drop和take的列表类;
"""


class MyList(object):
    def __init__(self, values=None):
        if values and isinstance(values, list):
            self.values = values  # 真正存储数据的地方
        else:
            self.values = []

    def __str__(self):
        if len(self.values) > 0:
            res = '['
            for x in self.values:
                current = '%s, ' % x
                res += current
            res = res[0:len(res) - 2]
            res += ']'
            return res
        else:
            return '[]'

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        if isinstance(item, slice):
            """
            上面提到, 在使用下标操作或切片操作时, 都会调用__getitem__方法;
            当使用切片操作时, 传进来的item就是一个slice类型(这是一个类), 它有start、end、stop等属性;
            但是其实不需要使用下面的方式进行取值, 直接在中括号中填入一个slice类型, 它会自动取值,
            (即, 只需要"return self.values[item]"就可以), 这里也只是为了演示传进来的item是slice类型;
            """
            return self.values[item.start:item.stop:item.step]
        else:
            return self.values[item]

    def __setitem__(self, key, value):
        """
        这里的key和__getitem__传入的item很像, 也可以传进来一个slice类型
        """
        self.values[key] = value

    def __delitem__(self, key):
        """
        这里的key和__getitem__传入的item很像, 也可以传进来一个slice类型
        """
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)


# __len__
my_list = MyList(values=['a', 'b', 'c'])
print('my_list = %s' % my_list)
print('len(my_list) = %s' % len(my_list))

print("##################################################")

# __getitem__
print('my_list[0] = %s' % my_list[0])
print('my_list[0::2] = %s' % my_list[0::2])

print("##################################################")

# __setitem__
my_list[0] = 1
print('my_list = %s' % my_list)
my_list[1:3] = [2, 3]
print('my_list = %s' % my_list)

print("##################################################")

# __delitem__
del my_list[0]
print('my_list = %s' % my_list)
del my_list[0::1]
print('my_list = %s' % my_list)

print("##################################################")

# __iter__
my_list = MyList(values=[1, 2, 3])
for x in my_list:
    print(x, end=' ')
print()

print("##################################################")

# __reversed__
my_list = MyList(values=[1, 2, 3])
print('my_list = %s' % my_list)
print('reversed(my_list): ', end='')
for x in reversed(my_list):
    print(x, end=' ')
print()

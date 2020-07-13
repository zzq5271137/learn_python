"""
自定义对象的序列化和持久化
"""

import pickle

"""
自定义对象的序列化和持久化:
自己定义的类的对象, 默认是不能持久化到磁盘中的, 因为自定义的类的对象无法直接使用pickle模块进行序列化和反序列化;
如果想使用pickle模块对自定义的类的对象进行持久化, 必须要实现两个魔术方法:
1. __getstate__(self):
   在使用pickle.dump()将对象存储到磁盘中的时候会自动调用这个方法, 会将这个方法的返回值存储到磁盘中;
   这个方法的返回值应该是默认可以持久化的数据类型, 例如: 整型、浮点型、字符串、字典、列表、元组等;
2. __setstate__(self, state):
   在使用pickle.load()从磁盘中加载对象的时候会自动调用这个方法; 会将从磁盘中读出的值以参数的形式传进来(state参数); 
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '<name: %s, age: %s>' % (self.name, self.age)

    def __getstate__(self):
        return {
            'name': self.name,
            'age': self.age
        }

    def __setstate__(self, state):
        self.name = state['name']
        self.age = state['age']


# 将对象写入磁盘中
with open('11-pickle_02_data.pkl', 'wb') as fp:
    p1 = Person('zzq', 27)
    pickle.dump(p1, fp)

# 从磁盘中加载对象
with open('11-pickle_02_data.pkl', 'rb') as fp:
    p1 = pickle.load(fp)
    print(p1)

"""
Python中哪些类型是能够直接序列化的: 列表、字典、字符串、元组、整型、集合、浮点类型、布尔类型
"""

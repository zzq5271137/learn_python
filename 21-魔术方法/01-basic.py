"""
常规魔术方法
"""

"""
魔术方法简介:
魔术方法是Python内置的一些特殊方法, 都是以"__xxx__"的形式命名的, 在自定义类的时候按照需要进行重写,
可以实现相应的功能; 

常规魔术方法/魔术属性:
1. __init__魔术方法:
   创建类实例对象后自动调用的初始化方法;
2. __del___魔术方法:
   析构方法, 销毁对象前(对象内存即将被释放前)自动调用的方法;
3. __new__魔术方法:
   用来创建一个对象的方法, 会返回一个实例对象;
4. __class__魔术属性:
   可以拿到当前对象所属的类的引用, (注意, 拿到的不是当前对象所属的类的类名, 而是所属的类的引用, 可以用它创建实例的);
5. __iter__魔术方法:
   返回一个迭代器对象, 可迭代的对象必须要有的方法, 也是迭代器对象必须要有的方法;
6. __next__魔术方法:
   迭代器对象在被遍历时, 每遍历一次都会调用这个方法, 是迭代器对象必须要有的方法;
7. __str__魔术方法:
   在打印某个对象的时候(调用print(obj)的时候或者调用str(obj)获得返回值的时候), 
   默认打印出的是这个对象所属类的名字以及这个对象的内存地址; 如果想要自定义打印出的内容, 可以重写__str__方法;
   (类似于Java的toString()方法);
8. __repr__魔术方法:
   这个魔术方法是用来表述一个对象在内存中的展示形式的, 用于给机器看的; 有下面两个小例子:
   a. 在终端定义了一个类, 重写了__repr__方法, 然后初始化了一个对象, 然后输入这个对象接着直接按回车, 
      这时候就会调用__repr__方法;
   b. 在编辑器中, 如果将一个变量创建完之后放入一个列表, 再打印这个列表, 那么会打印这个列表中所有的对象,
      这个时候就会调用__repr__方法;
9. __dict__魔术属性:
   这个属性装的是某个对象的所有用户自定义的属性及其对应的值(注意是自定义的属性), 以字典的形式展示;
   要和dir()函数做区分, dir()函数返回的是这个对象所有的属性的属性名, 包括内置的一些属性;
10. __slots__魔术属性:
    详见19-面向对象进阶/04-__slots__.py
"""


class Person1(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '我叫%s, 年龄是%d' % (self.name, self.age)

    def __repr__(self):
        return 'Person(%s, %d)' % (self.name, self.age)


# __str__
p1 = Person1('zzq1', 27)
print(p1)  # 这里会调用我们重写的__str__方法
p1_str = str(p1)  # 这里会调用我们重写的__str__方法
print(p1_str)

print("###############################################")

# __repr__
p2 = Person1('zzq2', 30)
p_list = [p1, p2]
print(p_list)  # 这里会调用我们重写的__repr__方法

print("###############################################")

# __dict__
print(p1.__dict__)
print(dir(p1))

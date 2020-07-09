"""
自定义元类
"""

"""
注意:
在Python2和Python3中, 给类定义元类的方式不一样; Python2中, 是添加一个__metaclass__属性, 例如:
    class Foo(object):
        __metaclass__ = my_metaclass
Python3中, 是在类签名的括号里, 在继承类的后面, 添加一个"metaclass=my_metaclass", 例如:
    class Foo(object, metaclass=my_metaclass):
        pass
"""


# 用函数的形式自定义元类
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
    将所有的类属性的名字都转为大写形式, 然后返回一个类对象
    """
    attrs = ((name, value) for name, value in future_class_attr.items() if
             not name.startswith('__'))
    uppercase_attrs = dict((name.upper(), value) for name, value in attrs)
    return type(future_class_name, future_class_parents, uppercase_attrs)


class Foo(object, metaclass=upper_attr):
    country = 'China'


# print(Foo.country)  # 会报错
print(Foo.COUNTRY)


# 用类的形式自定义元类
class UpperAttrMetaclass(type):
    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if
                 not name.startswith('__'))
        uppercase_attrs = dict((name.upper(), value) for name, value in attrs)
        return super().__new__(cls, future_class_name, future_class_parents, uppercase_attrs)


class Bar(object, metaclass=UpperAttrMetaclass):
    country = 'China'


# print(Bar.country)  # 会报错
print(Bar.COUNTRY)

"""
通常, 我们会使用类的形式自定义元类
"""

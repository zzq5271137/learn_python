"""
__metaclass__属性
"""

"""
你在写一个类的时候可以为其添加__metaclass__属性, 比如:
    class Foo(object):
        __metaclass__ = something
如果你这么做了, Python就会用该元类来创建Foo; 你首先写下class Foo(object), 但是类对象Foo还没有在内存中创建,
Python会在类的定义中寻找有没有__metaclass__属性, 如果找到了, 就用该元类创建Foo, 如果没找到,
就用内建的元类type来创建Foo; 更详细的地说, 当你写了如下代码:
    class Foo(Bar):
        pass
Python会做如下操作: 看一看Foo中有__metaclass__属性吗？如果有, Python会在内存中通过__metaclass__创建一个名为Foo的类对象;
如果Python没有找到__metaclass__属性, 它会继续在Bar类(父类)中寻找__metaclass__属性, 并做和前面同样的判断和操作;
如果Python在任何父类中都找不到__metaclass__属性, 它就会在模块层次中取寻找__metaclass__, 并做和前面同样的判断和操作;
如果还是找不到__metaclass__, Python就会用内置的type来创建Foo的类对象;

那么, 你的自定义元类中需要放置些什么代码呢？答案是, 可以创建一个类的东西; 那么, 什么东西可以创建一个类呢？
答案是type, 或者任何使用到type或者子类话type的东西都可以(即, 元类不一定是一个类, 也可以是一个函数,
示例详见: 09-my_metaclass.py)

注意:
在Python2和Python3中, 给类定义元类的方式不一样; Python2中, 是添加一个上面说的__metaclass__属性, 例如:
    class Foo(object):
        __metaclass__ = my_metaclass
Python3中, 是在类签名的括号里, 在继承类的后面, 添加一个"metaclass=my_metaclass", 例如:
    class Foo(object, metaclass=my_metaclass):
        pass
"""

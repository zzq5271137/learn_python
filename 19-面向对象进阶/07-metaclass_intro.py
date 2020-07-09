"""
元类介绍
"""

"""
什么是元类:
前面提到, 类也是对象, 那么既然是对象, 是谁创建了它呢？元类就是创建类的"东西", 元类就是类的类,
可以这样认为:
    MyClass = MetaClass()
    MyObject = MyClass()
我们在19-面向对象进阶/05-dynamic_create_class.py中使用type()来创建类, 这是因为type实际上就是一个元类,
type就是Python在背后用来创建所有类的元类(这就是为什么"print(type(MyClass))"打印的是"<class 'type'>");
为什么type是小写呢？这也许是为了和str或者int的命名保持统一, str是用来创建字符串对象的类, int是用来创建整数对象的类,
type就是用来创建类对象的类; 你可以通过检查__class__属性来看这一点(__class__可以拿到当前对象所属的类的引用); 
Python中的所有东西(注意是所有!!)都是对象, 包括整数、字符串、函数以及类, 他们全都是对象, 而且他们都是从一个类创建而来(即type);
(如果不指定__metaclass__属性, 那么所有类对象的元类默认都是内建元类type)
"""


def bar():
    pass


a = 35
print(a.__class__)  # <class 'int'>
name = 'bob'
print(name.__class__)  # <class 'str'>
print(bar.__class__)  # <class 'function'>
Foo = type('Foo', (), {})
foo_instance = Foo()
print(foo_instance.__class__)  # <class '__main__.Foo'>

# 对于以上任意一个__class__的__class__又是什么呢？是"<class 'type'>"; 为什么呢？
# 因为, __class__拿到的是当前对象所属的类的引用(详见06-__class__.py), 所以,
# foo_instance.__class__返回的就是Foo类, 而Foo.__class__自然就是type,
# 因为type是Python的内建元类, 是它创建的Foo类对象;
print(a.__class__.__class__)
print(name.__class__.__class__)
print(bar.__class__.__class__)
print(foo_instance.__class__.__class__)

"""
因此, 元类就是创建类的东西, 是类的类; type就是Python的内建元类, 当然了, 你也可以创建自己的元类
"""

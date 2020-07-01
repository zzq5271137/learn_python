"""
类和对象的基本使用
"""

"""
定义一个类的语法是使用class关键字, 开发者自己定义的类, 必须继承自object类, object类是Python中所有类的基类;
类中所有的方法都要以self作为第一个参数, 这是规定; self代表的是当前的对象(有点像Java中的this);
"""


# Python的继承是写在类名后的圆括号中的
class Person(object):  # object类是Python中所有类的基类
    def __init__(self, name, age, style):  # Python的类的构造方法
        # 类的属性的定义
        self.name = name
        self.age = age
        self.style = style
        print("构造函数, self={}".format(id(self)))  # self代表的是当前的对象

    def eat(self):
        print(u'我是%s, 我吃饭比较%s' % (self.name, self.style))


# 创建对象
p1 = Person(name='张三', age=18, style='文静')  # 当对象创建完毕(分配好内存空间)后, 自动调用__init__()构造方法去做初始化工作
print("创建对象, p1={}".format(id(p1)))  # id()函数返回对象的唯一标识符, 标识符是一个整数
p1.eat()
p1.gender = '男'  # 在Python中, 也可以直接给对象添加属性(但也仅仅是这个对象有这个属性, 新创建的对象没有)

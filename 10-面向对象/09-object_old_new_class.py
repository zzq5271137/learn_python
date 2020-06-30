# coding: utf-8

"""
旧式类与新式类
"""

"""
首先, Python3中没有旧式类与新式类的区别, 以下讨论的旧式类与新式类之间的区别, 都是在Python2环境中运行代码的基础上;
"""


# 旧式类(没有继承自任何类的类, 是旧式类, 在Python2.2版本之前, 所有的类都是旧式类)
class Person:
    def __init__(self, name):
        self.name = name


# 继承自旧式类的类依然是旧式类
class Teacher(Person):
    def __init__(self, name, teacherid):
        # super(Teacher, self).__init__(name)  # 在旧式类中, 不能使用super()
        Person.__init__(self, name)  # 旧式类中, 调用父类方法的方式, 即, 父类类名.父类方法名(self, 其他参数)
        self.teacherid = teacherid


# 新式类(直接或间接继承自object类的类, 就是新式类)
class Student(object):
    def __init__(self, name):
        self.name = name


t1 = Teacher('zzq', '123')

# 对于旧式类, 这两个打印的不一样
print(type(t1))  # <type 'instance'> (只要你是一个旧式类, 那么通过type()函数得到的类型都是instance)
print(t1.__class__)  # __main__.Teacher (__class__属性是自带的属性, 代表类的名称)

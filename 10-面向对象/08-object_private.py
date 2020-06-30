"""
子类不能继承父类的私有属性和方法
"""


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def __jump(self):
        print("%s ready to jump..." % self._name)


class Student(Person):
    def intro(self):
        print("我叫%s, 我是个学生." % self._name)  # 受保护的属性和方法可以继承
        # print("今年%s岁." % self.__age)  # 私有属性不能继承, 这里会报错
        # self.__jump()  # 私有方法不能继承, 这里会报错


s1 = Student('zzq', 27)
s1.intro()

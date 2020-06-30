"""
Python类的继承(面向对象特性之继承)
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("{}在吃饭".format(self.name))


class Student(Person):
    def intro(self):
        print("我叫{}, 今年{}岁, 是一名学生.".format(self.name, self.age))  # 继承了父类的属性


s1 = Student('zzq', 27)
s1.eat()  # 继承了父类的方法
s1.intro()

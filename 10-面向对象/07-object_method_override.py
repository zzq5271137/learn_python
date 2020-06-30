"""
重写父类方法
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("[父类方法]我叫{}, 今年{}岁".format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, studentid):
        super(Student, self).__init__(name, age)  # 调用父类的构造方法
        self.studentid = studentid

    def intro(self):  # 重写了父类的intro()方法
        super(Student, self).intro()  # 调用父类的intro()方法
        print("[子类方法]我是一名学生, 学号是{}".format(self.studentid))


s1 = Student('zzq', 27, '820064')
s1.intro()

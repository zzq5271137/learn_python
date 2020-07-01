"""
重写父类方法
"""


class Person(object):
    species = '人类'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("[父类实例方法]我叫{}, 今年{}岁".format(self.name, self.age))

    @classmethod
    def sayhello(cls):
        print("[父类类方法]你好, 我是%s" % cls.species)


class Student(Person):
    def __init__(self, name, age, studentid):
        super(Student, self).__init__(name, age)  # 调用父类的构造方法
        self.studentid = studentid

    def intro(self):  # 重写了父类的intro()方法(实例方法)
        super(Student, self).intro()  # 调用父类的intro()方法(实例方法)
        print("[子类实例方法]我是一名学生, 学号是{}".format(self.studentid))

    @classmethod
    def sayhello(cls):  # 重写了父类的sayhello()方法(类方法)
        super(Student, cls).sayhello()  # 调用父类的sayhello()方法(类方法)
        print("[子类类方法]我的职业是学生")


s1 = Student('zzq', 27, '820064')
s1.intro()
print("#######################################")
s1.sayhello()
Student.sayhello()

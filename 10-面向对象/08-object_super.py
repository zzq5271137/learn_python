"""
super()的使用
"""

"""
super()函数的描述:
super()函数是用于调用父类(超类)的一个方法; 想要调用父类方法, 可以直接使用父类类名调用, 
但是super()的一大好处在于, 当父类的名字修改时, 其继承类不用修改调用方法的语句;
在多继承下, 使用super()函数会涉及到查找顺序(MRO)的问题; MRO(Method Resolution Order)就是类的方法解析顺序表,
其实也就是继承父类方法时的顺序表, 可以通过查看__mro__类属性或者通过类名调用mro()方法来查看方法解析顺序表的内容;

super()函数的语法:
super(type, object), 其中: 
1. type: 
   类, 即调用哪一个类的父类的方法
2. object: 
   实例对象, 即哪个对象去调用方法;
   如果调用本类父类的方法, 一般是self; 
   如果不是调用本类父类的方法, 例如调用本对象中的某个属性(该属性为一个对象)的父类的方法, 则需要填入那个相关属性,
   而且上面的type参数要填该属性的类;
Python3和Python2的一个区别是, 如果是调用本类父类的方法, Python3可以使用直接使用super().xxx代替super(Class, self).xxx;
"""


class Animal(object):
    def __init__(self, name):
        self.name = name

    def petintro(self):
        print("宠物姓名: %s" % self.name)


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)  # 调用父类的构造方法

    def petintro(self):
        print("宠物种类: 狗")


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("我叫{}, 今年{}岁".format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, studentid, pet):
        super().__init__(name, age)  # 调用父类的构造方法
        self.studentid = studentid
        self.pet = pet

    def intro(self):
        # super(Student, self).intro()  # 调用本类父类的实例方法
        super().intro()  # 调用本类父类的实例方法(Python3中可以省略super()函数的参数)
        print("我是个学生, 我的学号是{}, 我有只宠物, 宠物信息:".format(self.studentid))
        super(Dog, self.pet).petintro()  # 调用非本类父类的实例方法
        self.pet.petintro()


dog = Dog('大黄')
student = Student('zzq', 27, '820064', dog)
student.intro()

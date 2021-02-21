"""
实例方法、类方法、静态方法
"""

"""
实例方法: 属于实例的方法, 只能通过对象去调用, 不能通过类名去调用; 
         在定义实例方法时第一个参数必须为self(代表当前实例对象);
类方法: 属于整个类的方法, 通过类名去调用, 也可以通过实例对象去调用; 
       定义类方法需要通过"@classmethod"装饰器, 并且第一个参数必须为cls(代表当前类);
静态方法: 就是类中的一个普通的函数, 只不过写在了一个类中;
        定义静态方法需要使用"@staticmethod"装饰器, 不需要传入任何默认参数;
        可以认为静态方法就是一个普通的函数, 它的操作不涉及实例属性, 也不应该涉及类属性, 
        虽然使用诸如Person.species的方式可以访问和修改类属性, 但是不推荐这样写,
        如果需要涉及类属性, 请将方法声明声类方法;
"""


class Person(object):
    species = 'Human'

    def __init__(self, name):
        self.name = name

    def eat(self):  # 这就是实例方法, 在定义实例方法时第一个参数必须为self
        print('{}正在吃饭'.format(self.name))

    @classmethod
    def greet(cls):  # 这就是类方法, 通过"@classmethod"装饰器来定义, 并且第一个参数必须为cls
        print("hello world")
        if cls.species == 'Human':  # cls代表当前类, 无论是通过类名还是实例对象调用该方法, cls都代表当前类
            cls.__change_species()  # 类方法内不能调用实例方法, 但可以调用类方法或静态方法

    @classmethod
    def __change_species(cls):
        print("验证cls代表当前类, 尝试修改类属性species, 修改前: Person.species = %s" % Person.species)
        cls.species = 'Dog'
        print("修改后: Person.species = %s" % Person.species)

    @staticmethod
    def die():  # 这就是静态方法, 通过"@staticmethod"装饰器来定义, 不需要传入任何默认参数
        print("People will be dead at last.")


# 实例方法的调用
print("实例方法的调用")
p1 = Person('zzq')
p1.eat()  # 只能通过实例来调用

print("#######################################")

# 类方法的调用
print("类方法的调用")
p1.greet()  # 可以通过实例来调用
Person.greet()  # 可以通过类名来调用

print("#######################################")

# 静态方法的调用
print("静态方法的调用")
p1.die()  # 可以通过实例来调用
Person.die()  # 可以通过类名来调用

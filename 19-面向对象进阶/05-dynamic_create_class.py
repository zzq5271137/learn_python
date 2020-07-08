"""
动态地创建类
"""

"""
类也是对象:
在Python中, 任何东西都是对象, 包括一个整型、字符串、函数等等, 都是对象; 类, 也是对象;
当你使用class关键字定义一个类的时候, Python解释器在执行该文件的时候就会创建一个对象;
下面的代码段:
    class Person(object):
        pass
当Python解释器执行这个文件碰到这段代码时, 它会在内存中创建一个对象, 名字就叫Person,
这个对象(类)自身拥有创建对象(类实例)的能力, 而这就是为什么我们称Person为一个类的原因;
但是, Person的本质仍然是一个对象, 于是你可以对它做如下操作:
1. 将它赋值给一个变量
2. 拷贝它
3. 为它增加属性
4. 将它作为函数参数进行传递

既然类也是对象, 所以可以像动态地创建普通类实例对象那样, 动态地创建类, 如下所示
"""


def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass

        return Foo  # 注意, 没有加圆括号, 返回的是一个类
    else:
        class Bar(object):
            pass

        return Bar


MyClass = choose_class('foo')
print(MyClass)
print(MyClass())

print("######################################################################")

"""
以上方式还不够动态, 因为你仍然需要自己编写整个类的代码; 由于类也是对象, 所以他们必须是通过什么东西来生成才对;
当你使用class关键字时, Python解释器在运行这个文件时会自动创建这个对象(类); 但就和Python中的大多数事情一样,
Python仍然提供给你手动处理的方法; 还记得内建函数type()吗, 这个古老但强大的函数能够让你知道一个对象的类型是什么;
"""


class Person(object):
    pass


print(type(Person))
print(type(Person()))

"""
type()函数还有一种完全不同的能力, 它能动态地创建类; type()函数可以接收一个类的描述作为参数, 然后返回一个类;
type()函数可以像这样工作:
    type(类名, 父类的元组（针对继承/多继承的情况, 可以为空）, 包含属性的字典（名称和值）)
"""
print("type()函数动态创建类")
Student = type('Student', (object,), {'name': 'zzq', 'age': 27, 'studentid': '820064'})
s1 = Student()
print("我是个学生, 名字是%s, 年龄%d, 学号是%s" % (s1.name, s1.age, s1.studentid))

"""
上面的type()函数创建Student类, 等价于下面的写法:
    class Student(object):
        name = 'zzq'
        age = 27
        studentid = '820064'
"""

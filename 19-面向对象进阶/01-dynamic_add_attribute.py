"""
动态添加属性
"""

"""
动态添加属性:
就是这属性不是在定义类的时候添加的, 而是而是创建完这个对象后, 在程序运行过程中添加的; 动态添加属性有两种方法, 
第一种是直接通过"对象名.属性名", 第二种是通过setattr()函数添加;
"""


class Person(object):
    def __init__(self, name):
        self.name = name


p1 = Person('zzq')

# 第一种, 通过"对象名.属性名"的方式动态添加属性
p1.age = 27

# 第二种, 通过setattr()函数的方式动态添加属性
if not hasattr(p1, 'studentid'):
    setattr(p1, 'studentid', '820064')

"""
hasattr()函数是用来判断一个对象是否有某个属性; setattr()函数是用来给某个对象添加属性, 并且指定这个属性的值;
getattr()函数是用来访问一个对象的某个属性, 并且可以设定一个默认值, 如果这个属性不存在, 则返回这个默认值;
"""
print('My name is %s, my age is %d, my studentid is %s' % (p1.name, p1.age,
                                                           getattr(p1, 'studentid', '000000')))

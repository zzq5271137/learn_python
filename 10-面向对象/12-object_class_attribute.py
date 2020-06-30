"""
类属性和实例属性
"""

"""
实例属性: 绑定到实例对象上的属性就是实例属性
类属性: 属于整个类的属性, 类似于Java的static属性
"""


class Person(object):
    species = 'Human'  # 这就是类属性, 属于整个类的属性, 类似于Java的static属性

    def __init__(self, name):
        # 这个name就是实例属性, 因为它绑定到了实例对象(self指代当前实例对象)上
        # 补充: 其实以这种形式绑定属性和下面的"p1.age = 27"是同一种方式,
        #      只不过__init__()方法在每个对象创建时都会被调用, 所以每个Person对象都会绑定name属性,
        #      但其实从根本上讲, 实例属性只对当前对象有作用;
        self.name = name


p1 = Person("zzq")
p1.age = 27  # 这也是实例属性(但是以这种方式绑定的实例属性真的就只有当前对象可以使用了)

"""
类属性的访问与修改:
可以通过类名来访问类属性, 也可以通过实例对象来访问类属性, 但是不推荐使用实例对象来访问类属性,
因为通过实例对象来访问类属性的本质是这样的, 假如类属性名为species, 当使用实例对象来访问species时,
如果该类没有一个名为species的实例属性, 那么它这次访问的就是类属性, 这暂时没有什么问题;
但是一旦想通过实例对象去修改类属性, 例如"p1.species = 'Dog'"这种形式, 实际上这修改的不是类属性,
而是为p1实例添加了一个名为species的实例属性, 并且赋值为'Dog', 这个species和类属性species是没有什么关系的;
所以, 无论是访问还是修改类属性, 都应该直接使用类名;
"""
print("Before, Person.species = %s" % Person.species)
p1 = Person('zzq1')
p2 = Person('zzq2')
p1.species = 'Dog'
print("p1.species = %s" % p1.species)
p2.species = 'Cat'
print("p2.species = %s" % p2.species)
print("After, Person.species = %s" % Person.species)

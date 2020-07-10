"""
控制属性访问的魔术方法
"""

"""
控制属性访问的魔术方法:
1. __getattr__(self, item)魔术方法:
   在访问一个对象的的某个属性时, 如果这个属性不存在, 那么就会执行__getattr__方法(包括在类中的方法中使用"self.xxx"), 
   将属性的名字传进去(item参数); 如果这个属性存在, 就不会调用__getattr__方法;
2. __setattr__(self, key, value)魔术方法:
   只要给一个对象的属性设置值, 那么就会调用这个方法(包括在类中的方法中使用"self.xxx = xxx");
   但需要注意的是, 不要在这个方法中使用"self.xxx = xxx"的形式, 因为会产生递归调用; 如果想要在这个方法内给属性设置值, 
   应该使用__dict__这个魔术属性, 例如: self.__dict__['name'] = 'new_zzq'
3. __getattribute__(self, item)魔术方法:
   这个魔术方法是, 只要你访问了一个对象的属性, 不管这个属性存不存在, 都会执行这个方法(包括在类中的方法中使用"self.xxx");
   所以在写这个方法的时候要小心循环调用; 这个方法只能在新式类中使用;
"""


class Person(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        res = '['
        for key, value in self.__dict__.items():
            entry = '%s=%s, ' % (key, value)
            res += entry
        res = res[0:(len(res) - 2)]
        res += ']'
        return res

    def __getattr__(self, item):
        if item == 'country':
            return 'China'
        else:
            return None

    def __setattr__(self, key, value):
        if key == 'age':
            if value >= 18:
                self.__dict__['is_adult'] = True
            else:
                self.__dict__['is_adult'] = False
        self.__dict__[key] = value

    def __getattribute__(self, item):
        return super().__getattribute__(item)


p1 = Person('zzq')
print(p1)
print(p1.name)
print(p1.country)
p1.age = 27
print(p1)

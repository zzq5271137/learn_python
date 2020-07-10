"""
比较运算符魔术方法
"""

"""
比较运算符魔术方法:
1. __cmp__(self, other)魔术方法:
   这个方法类似于Java中的compareTo()方法, 重写该方法, 可以以自定义的方式比较两个对象,
   如果两个对象相等, 返回0, 如果self > other, 返回正整数(通常使用1), 反之, 返回负整数(通常使用-1);
   重写了这个方法后, 就可以直接使用比较运算符去比较两个对象了(例如p1 > p2、p1 == p2等); 当然也可以直接调用此方法进行比较;
   这个方法是Python2中用作对象比较的方法, 在Python3中已弃用, 因为在Python3中, 将__cmp__方法拆成了各种方法,
   即每种比较运算符都有一个对应的魔术方法, 细化了操作(详见下方);
2. __eq__(self, other)魔术方法:
   在使用"=="比较运算符比较两个对象时自动调用的方法, 如果成立, 返回True, 反之, 返回False;
3. __ne__(self, other)魔术方法:
   在使用"!="比较运算符比较两个对象时自动调用的方法, 如果成立, 返回True, 反之, 返回False;
4. __lt__(self, other)魔术方法:
   在使用"<"比较运算符比较两个对象时自动调用的方法, 如果成立, 返回True, 反之, 返回False;  
5. __gt__(self, other)魔术方法:
   在使用">"比较运算符比较两个对象时自动调用的方法, 如果成立, 返回True, 反之, 返回False;
6. __le__(self, other)魔术方法:
   在使用"<="比较运算符比较两个对象时自动调用的方法, 如果成立, 返回True, 反之, 返回False;
7. __ge__(self, other)魔术方法:
   在使用">="比较运算符比较两个对象时自动调用的方法, 如果成立, 返回True, 反之, 返回False;
"""


class Person(object):
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __eq__(self, other):
        return self.age == other.age and self.height == other.height


p1 = Person('zzq1', 27, 170)
p2 = Person('zzq2', 27, 170)
print(p1 == p2)

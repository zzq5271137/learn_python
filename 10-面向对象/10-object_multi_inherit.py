"""
多继承
"""


class Ma(object):
    def run(self):
        print("奔跑")

    def eat(self):
        print("吃草")


class Lv(object):
    def lamo(self):
        print("拉磨")

    def eat(self):
        print("吃麦秆")


# Python中的类是可以多继承的, 子类会继承所有父类的属性和方法
class LuoZi(Ma, Lv):
    def eat(self):
        # super(LuoZi, self).eat()  # 如果使用super(), 会根据__mro__属性保存的调用顺序去决定调用哪一个父类的方法
        Lv.eat(self)  # 或者, 可以手动指定调用哪个父类的方法


luozi = LuoZi()
luozi.run()
luozi.lamo()

# 如果子类(LuoZi类)中没有eat()方法, 就会调用父类的eat()方法;
# 但是这里继承的两个类中都有一个eat()方法, 那么会调用哪个呢?
# 答案是, 会根据__mro__属性保存的调用顺序去决定调用哪一个父类的方法(__mro__属性保存了方法执行的调用顺序)
print(LuoZi.__mro__)
luozi.eat()

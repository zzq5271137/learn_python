"""
Python的多态(面向对象特性之多态)
"""

"""
拿Java举例, 多态就是同一个接口(父类), 有不同的实现类(子类)而去实现不同的逻辑, 然后在定义参数时, 
将参数类型定义为接口(父类)的类型, 这样, 只要是实现了该接口(继承自该父类)的类都可以作为参数传入进去,
从而会根据传入的参数的具体类型的不同而实现不同的逻辑; 这样的编码更灵活、更松耦合、可扩展性更强; 这就是多态;
但是这些是针对于诸如Java、C++这种强类型语言来说的, 因为在这些强类型语言中, 定义方法参数时必须指明其类型;
而Python属于弱类型语言, 不需要指明变量或者参数的类型, 所以"多态"的概念在Python中就没那么强了;
但是Python中也是存在与多态相似的概念, 即"鸭子类型"; 鸭子类型是指, 不管你这个传进来的对象的类型是什么,
只要你有相应的方法, 我就会执行该方法;
"""


class ChengYaoJin(object):
    def stroke(self):
        print("程咬金的大招")


class XiangYu(object):
    def stroke(self):
        print("项羽的大招")


def play(champion):
    # 可以看到, ChengYaoJin类和XiangYu类之间是没什么关系的, 他们没有继承自同一个父类,
    # 但是依然可以正确执行各自的stroke()方法, 这就是"鸭子类型"
    champion.stroke()


chosen = input(u'请选择英雄: ')
champ = None
if chosen == '1':
    champ = ChengYaoJin()
elif chosen == '2':
    champ = XiangYu()
else:
    print("选择错误")

play(champ)

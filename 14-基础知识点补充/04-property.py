"""
property装饰器
"""

"""
我们在获取和设置属性时, 使用get和set方法(详见03-getter_setter.py); 但是这有弊端, 
因为我们要对属性写好多的get和set方法, 而且我们在获取和设置属性时, 还要记得必须要使用get和set方法,
因为在get和set方法内部执行了其他的一些内部逻辑, 如果我们直接obj.attr的方式去获取属性, 
或者obj.attr = 'whatever'的方式去设置属性, 那些内部逻辑就不会被执行, 程序运行就会有问题;
更好的方式是, 我们依然使用obj.attr的方式去获取属性, 或者obj.attr = 'whatever'的方式去设置属性,
并且那些相应的内部逻辑也会被自动执行; 这就是property装饰器的作用;
"""


# 模拟小飞机游戏
class Plane(object):
    def __init__(self):
        """
        使用property装饰器时, 对象内部的使用的属性名和外部使用的属性名不能一样, 否则会出现递归调用的死循环,
        即"RecursionError: maximum recursion depth exceeded"的错误;
        """
        self._alive = True  # 记得属性名前面加一个下划线, 表示受保护的属性(两个下划线表示私有属性)
        self._score = 0

    # 将get_alive()方法改名为alive(), 并加上"@property"装饰器, 将其设置为alive属性,
    # 也就是说, property装饰器将方法变为属性, 方法名就是属性名, 以后调用temp = obj.alive, 就会自动调用此方法;
    # 注: 在此方法内部使用的属性不能为"alive", 因为调用obj.alive, 就相当于调用了此方法, 就会出现递归调用的死循环,
    # 即"RecursionError: maximum recursion depth exceeded"的错误;
    @property
    def alive(self):  # 原get_alive()方法
        if not self._alive:
            self._cancel_schedule()
        return self._alive

    def _cancel_schedule(self):
        print("取消事件调度")

    # 将set_alive()方法改名为alive()(和上面@property设置的属性名/方法名相同), 并添加"@alive.setter"装饰器,
    # 其中"@alive"部分, 和上面@property设置的属性名/方法名相同, 也就是说, property装饰器将方法变为属性,
    # 方法名就是属性名, 以后调用obj.alive = whatever, 就会自动调用此方法;
    # 注: 在此方法内部使用的属性不能为"alive", 因为调用obj.alive = whatever, 就相当于调用了此方法,
    # 就会出现递归调用的死循环, 即"RecursionError: maximum recursion depth exceeded"的错误;
    @alive.setter
    def alive(self, alive):  # 原set_alive()方法
        self._alive = alive
        if not alive:
            self._die_action()

    def _die_action(self):  # 记得方法名前面加一个下划线, 表示受保护的方法(两个下划线表示私有方法)
        """
        飞机死亡时的动画效果;
        其实这个方法也可以在外面调用, 但是讲道理, 这个效果应该是飞机在死亡时自己去执行, 而不是由外面调用,
        所以这个方法的调用写在了alive的set方法里面(这是面向对象的编程逻辑);
        """
        print('爆炸')

    @property
    def score(self):  # 原get_score()方法
        if not self._alive:
            self._cancel_schedule()
        return self._score

    @score.setter
    def score(self, score):  # 原set_score()方法
        self._score = score
        self._update_score_brand(score)

    def _update_score_brand(self, score):
        """
        更新得分时, 需要去更新得分榜上的值显示给玩家
        """
        print("当前得分: %d" % score)


p1 = Plane()
hit = True  # 飞机中弹
if hit:
    p1.alive = False
    p1.score = p1.score + 100

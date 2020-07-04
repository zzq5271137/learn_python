"""
get和set方法
"""

"""
为什么需要get和set方法呢？因为我们在获取或者设置对象的某个属性时, 我们可能需要做一些事情; 比如下面的模拟小飞机游戏,
我们在获取alive属性时, 如果飞机已死亡, 我们需要取消事件调度; 或者我们在设置alive时, 如果设置的值是False,
我们需要执行爆炸的动画; 但这些事情应该都是对象内部自己完成的, 不应该是由外部调用的, 这是面向对象的思想;
所以, 我们可以在alive的get和set方法内去做相应的事情;
但是这还是存在问题, 因为如果业务逻辑复杂起来、对象的属性多起来, 我们就需要写好多好多的get和set方法;
这就是property装饰器诞生的原因, property装饰器就是为了解决属性和get、set方法的问题, 详见04-property.py
"""


# 模拟小飞机游戏
class Plane(object):
    def __init__(self):
        self.alive = True
        self.score = 0

    def get_alive(self):
        if not self.alive:
            self._cancel_schedule()
        return self.alive

    def _cancel_schedule(self):
        print("取消事件调度")

    def set_alive(self, alive):
        self.alive = alive
        if not alive:
            self._die_action()

    def _die_action(self):  # 记得方法名前面加一个下划线, 表示受保护的方法(两个下划线表示私有方法)
        """
        飞机死亡时的动画效果;
        其实这个方法也可以在外面调用, 但是讲道理, 这个效果应该是飞机在死亡时自己去执行, 而不是由外面调用,
        所以这个方法的调用写在了alive的set方法里面(这是面向对象的编程逻辑);
        """
        print('爆炸')

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score
        self._update_score_brand(score)

    def _update_score_brand(self, score):
        """
        更新得分时, 需要去更新得分榜上的值显示给玩家
        """
        print("当前得分: %d" % score)


p1 = Plane()
hit = True  # 飞机中弹
if hit:
    p1.set_alive(False)
    p1.set_score(p1.get_score() + 100)

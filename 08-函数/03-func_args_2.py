"""
函数的参数
"""

"""
缺省的位置参数和缺省的关键字参数
缺省的位置参数: *args代表缺省的位置参数(一颗星代表缺省的位置参数, 名字其实可以随便取, 但是习惯叫这个),
              在函数体内部, 它是一个元组;
缺省的关键字参数: **kwargs代表缺省的关键字参数(两颗星代表缺省的关键字参数, 名字其实可以随便取, 但是习惯叫这个),
                在函数体内部, 它是一个字典;
"""


def printargs(*args, **kwargs):
    print(args)
    print("type of args: %s" % type(args))
    print(kwargs)
    print("type of kwargs: %s" % type(kwargs))


printargs(1, 2, 3, a=4, b=5)  # 位置参数必须在关键字参数前面

print("##################################################################")

"""
将缺省的位置/关键字参数继续往下传递(这里使用自定义装饰器来举例)
"""

user = {
    "is_login": True
}


def login_required(func):
    def wrapper(*args, **kwargs):
        """
        在定义函数时, 形参里接收缺省的位置/关键字参数, 即*args与**kwargs的写法, 表示他们可以接收任意个数的位置/关键字参数,
        但是args和kwargs本身, 分别是一个元组和一个字典; 如果将args和kwargs直接往下传递给函数func(),
        代表着给func()传递了两个参数, 即一个元组(args)和一个字典(kwargs);
        但是如果以*args和**kwargs的方式将参数传递给func(), 则是以多个(不定个数)参数的形式传递,
        即, 将args元组拆解成多个位置参数, 将**kwargs字典拆解成多个关键字参数, 然后传递给func();
        所以, 将自身接收到的*args与**kwargs继续向下传递时, 不同的方式(带不带*或**)会有截然不同的效果与意义;
        """
        if user["is_login"]:
            func(*args, **kwargs)
        else:
            print("跳转到登录页面")

    return wrapper


@login_required
def edit_user(username):
    print("用户信息修改成功, 新用户名: %s" % username)


@login_required
def add_num(num_a, num_b):
    print("两数之和为: %d" % (num_a + num_b))


edit_user('zzq')
add_num(3, 4)

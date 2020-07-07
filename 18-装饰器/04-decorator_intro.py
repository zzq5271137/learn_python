"""
装饰器
"""

"""
什么是装饰器:
装饰器利用了函数也可以作为参数传递的特性和闭包的特性, 可以让我们的函数在执行之前或者执行之后方便地添加一些代码;
这样就可以做很多事情了, 比如@classmethod装饰器可以将一个普通的方法设置为类方法,
@staticmethod装饰器可以将一个普通的方法设置为静态方法, 等等; 所以明白了装饰器的原理后,
我们就可以自定义装饰器, 从而实现我们自己的需求;

拿网站开发的例子来说, 我们经常会碰到一些页面或操作是需要用户认证后才可以访问的, 那么如果每次都在访问的视图函数中进行判断,
会很难维护和扩展; 例如下面的例子, 这里只有两个函数, 在真实场景中, 视图函数会非常非常多, 如果我们修改了需求,
比如这里如果用户尚未登录, 我想让它跳转到注册页面而不是登录页面, 那么将会有很多地方需要修改, 代码将很难进行维护和扩展; 
这时候我们就可以使用装饰器;
"""
user = {
    "is_login": False
}


def edit_user_0():
    if user["is_login"]:
        print("用户信息修改成功")
    else:
        print("跳转到登录页面")


def add_article_0():
    if user["is_login"]:
        print("文章添加成功")
    else:
        print("跳转到登录页面")


edit_user_0()
add_article_0()

print("###########################################################")

"""
使用一个单独的函数进行用户认证的方式对上面的方式进行改进; 这种方式优于上面的方式, 但是依然不够优雅和高效;
"""


def login_required_1(func):
    if user["is_login"]:
        func()
    else:
        print("跳转到登录页面")


def edit_user_1():
    print("用户信息修改成功")


def add_article_1():
    print("文章添加成功")


login_required_1(edit_user_1)
login_required_1(add_article_1)

print("###########################################################")

"""
使用装饰器对上面的方式进行改进(这里并不是装饰器的正确使用姿势, 但是这是装饰器的底层原理)
"""


def login_required_2(func):
    def wrapper():
        if user["is_login"]:
            func()
        else:
            print("跳转到登录页面")

    return wrapper


def edit_user_2():
    print("用户信息修改成功")


def add_article_2():
    print("文章添加成功")


login_required_2(edit_user_2)()
login_required_2(add_article_2)()

print("###########################################################")

"""
装饰器的正确使用姿势
"""


def login_required_3(func):
    def wrapper():
        if user["is_login"]:
            func()
        else:
            print("跳转到登录页面")

    return wrapper


@login_required_3
def edit_user_3():
    print("用户信息修改成功")


@login_required_3
def add_article_3():
    print("文章添加成功")


"""
装饰器函数的调用时机:
这里就不是普普通通的调用edit_user_3()函数了; 当edit_user_3()函数的上面标注了一个login_required_3装饰器,
那么在执行此文件时(注意并不是edit_user_3()函数被调用时, 而是在此文件被执行时),
它会自动地将edit_user_3()函数的引用传给login_required_3()函数, 然后login_required_3()函数返回一个闭包(wrapper()函数),
再将此闭包(wrapper()函数)赋值给edit_user_3; 所以, 当执行edit_user_3()函数时, 其实执行的是wrapper()函数;
"""
edit_user_3()
add_article_3()

# 注: 装饰器不仅可以修饰函数, 也可以修饰类中的方法

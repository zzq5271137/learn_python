"""
被装饰的函数带有参数
"""

user = {
    "is_login": True
}


def login_required(func):
    def wrapper(*args, **kwargs):
        if user["is_login"]:
            func(*args, **kwargs)  # 记得08-函数/03-func_args_2.py中讲到的缺省的位置/关键字参数继续向下传递的问题
        else:
            print("跳转到登录页面")

    return wrapper


@login_required
def edit_user(username):
    print("用户信息修改成功, 新用户名: %s" % username)


@login_required
def add_article(title, content):
    print("文章添加成功, 标题: {}, 内容: {}".format(title, content))


edit_user('zzq')
add_article('我是标题', '我是内容')

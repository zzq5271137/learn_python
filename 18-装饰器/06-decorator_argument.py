"""
给装饰器传递参数
"""

user = {
    "is_login": False
}

tokens = {
    "front_token": 'f123',
    "back_token": "b456"
}


def login_required(site='front', token=tokens["front_token"]):
    def outter_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            if user["is_login"]:
                func(*args, **kwargs)
            else:
                if site == 'front' and token == tokens["front_token"]:
                    print('跳转到前台登录页面')
                elif site == 'back' and token == tokens["back_token"]:
                    print('跳转到后台登录页面')
                else:
                    print('指令或token有误')

        return inner_wrapper

    return outter_wrapper


@login_required(site='back', token=tokens["back_token"])
def edit_user(username):
    print("用户信息修改成功, 新用户名: %s" % username)


# 如果不想传递参数(使用默认值), 也必须加圆括号; 因为只有加圆括号, 才表示执行login_required()函数,
# 只有执行了login_required()函数, 才会返回真正的装饰器(即outter_wrapper);
# @login_required
@login_required()
def add_article(title, content):
    print("文章添加成功, 标题: {}, 内容: {}".format(title, content))


edit_user('zzq')
add_article(title='我是标题', content='我是内容')

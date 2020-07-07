"""
案例: 模拟Flask的路由映射部分
"""

from functools import wraps

user = {
    "is_login": True
}


def login_required(func):
    @wraps(func)  # 这里必须加@wraps装饰器(请自行分析)
    def wrapper(*args, **kwargs):
        if user["is_login"]:
            func(*args, **kwargs)
        else:
            print("跳转到登录页面")

    return wrapper


class Flask(object):
    def __init__(self):
        self.url_views_maps = {}

    def route(self, url):
        """
        记得18-装饰器/04-decorator_intro.py的最后面, 讲到装饰器函数的调用时机,
        即, 当函数上面标注了装饰器, 那么当执行此文件时(注意并不是该函数被调用时, 而是执行此文件时),
        该函数会调用该装饰器的装饰器函数, 装饰器函数会返回一个闭包, 然后该函数的变量重新指向这个闭包,
        也即是, 执行此函数实际上执行的是装饰器函数返回的那个闭包函数;
        那么回到这个例子, 下面的index()函数和articlelist()函数都标注了route装饰器,
        所以在执行此文件时, 他们就会分别调用这里的route()函数, 然后运行route()函数里的逻辑,
        把他们传入的url和他们的方法名都存进url_views_maps中; 当下面执行run()方法时,
        url_views_maps中已经包含了这两个url和其对应的函数名;
        """

        def outter_wrapper(func):
            self.url_views_maps[url] = func.__name__

            @wraps(func)
            def inner_wrapper(*args, **kwargs):
                func(*args, *kwargs)

            return inner_wrapper

        return outter_wrapper

    def run(self):
        while True:
            url = input('请输入url: https://localhost:8080')
            if url == '':
                url = '/'
            view_func_name = self.url_views_maps.get(url)
            if view_func_name:
                exec(view_func_name + '()')  # exec()函数可以将传进来的东西当做Python代码来执行
            else:
                print('抱歉, 您访问的页面不存在')


app = Flask()


@app.route('/')
def index():
    print("index page")


@app.route('/articlelist')
def articlelist():
    print("article list page")


# 可以加多个装饰器(装饰器函数是从里到外执行的, 比如这里, 就先会执行login_required()函数)
@app.route('/edituser')
@login_required
def edituser():
    print("更改用户名成功")


app.run()

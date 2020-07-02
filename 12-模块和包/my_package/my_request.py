"""
在Python3中, 在同一个包中的模块如果要互相导入, 有两种方式:
1. 绝对路径的方式:
   即, from 包1.包2 import 模块名
   或者, import 包1.包2.模块名
   其中, 模块在包2下, 包2在包1下, 然后包1是在sys.path中的某个路径中可以找到的
2. 相对路径的方式:
   即: from . import 模块名
   (一个"."代表当前目录, 两个".."表示上级目录)
"""

from my_package.my_inner_package import my_whatever1  # 方式一(绝对路径)
import my_package.my_inner_package.my_whatever2  # 方式一(绝对路径)
from .my_inner_package import my_whatever3  # 方式二(相对路径)
from . import my_file  # 方式二(相对路径)

print("模块my_request被导入了")  # 如果你导入了某个包或模块, 那么Python会马上将那个模块中的代码立即执行一遍


def get_request(url):
    data = {'body': 'abc'}
    print('您的GET请求%s已经下载下来了, 数据为: %s' % (url, data))
    return data


def post_request(url):
    data = {'body': 'abc'}
    print('您的POST请求%s已经下载下来了, 数据为: %s' % (url, data))
    return data

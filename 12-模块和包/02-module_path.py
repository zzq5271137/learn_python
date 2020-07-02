"""
模块查找路径
"""

import sys
from my_package import my_request

"""
sys.path属性是一个列表, 每一项都是一个路径, 即在Python执行当前代码的时候会从哪些路径去查找包和模块(查找包和模块的路径);
比如上面的"from my_package import my_file", Python会从sys.path这个列表里的每一项(每一个路径)中去找有没有my_package这个包,
直到找到这个包或者尝试过了sys.path中的每一项(没找到, 报错);

注: 在PyCharm中, 将一个文件夹标注成Sources Root(右击某文件夹 -> Mark Directory as -> Sources Root),
可以将该文件夹的路径添加进sys.path, 也就是说扫描包的时候会扫描它;
"""
print(sys.path)

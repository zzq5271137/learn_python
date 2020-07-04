"""
__doc__与文档注释
"""


class Person(object):
    """
    写在这里的注释, 叫做文档注释, 会保存进类的__doc__变量中;
    (而且如果使用PyCharm, 在外部使用Person类的地方, 当鼠标悬浮在Person上面, 会显示这里的内容)
    """
    pass


print(Person.__doc__)

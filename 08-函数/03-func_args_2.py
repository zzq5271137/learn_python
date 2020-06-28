"""
函数的参数
"""


# 缺省的位置参数和缺省的关键字参数
# 缺省的位置参数: *args代表缺省的位置参数(一颗星代表缺省的位置参数, 名字其实可以随便取, 但是习惯叫这个),
#               在函数体内部, 它是一个元组;
# 缺省的关键字参数: **kwargs代表缺省的关键字参数(两颗星代表缺省的关键字参数, 名字其实可以随便取, 但是习惯叫这个),
#                在函数体内部, 它是一个字典;
def printargs(*args, **kwargs):
    print(args)
    print("type of args: %s" % type(args))
    print(kwargs)
    print("type of kwargs: %s" % type(kwargs))


printargs(1, 2, 3, a=4, b=5)  # 位置参数必须在关键字参数前面

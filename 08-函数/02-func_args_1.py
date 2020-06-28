"""
函数的参数
"""


# 位置参数与关键字参数
# 位置参数: 就是在调用函数时, 按照函数的形参给定的顺序进行传参
# 关键字参数: 就是在调用函数时, 按照函数的形参名称进行传参(参数的顺序可以随意)

def greet(name, greetstr):
    print("{}, {}".format(greetstr, name))


# 位置参数传参
greet("zzq", "Good morning")

# 关键字参数传参
greet(greetstr="Good night", name="zzq")

# 混合传参
greet("zzq", greetstr="Good afternoon")
# 混合参数的注意事项: 位置参数必须要在关键字参数的前面

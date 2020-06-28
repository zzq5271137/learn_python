"""
函数的参数
"""


# 函数的默认参数: 在定义函数时, 给函数的参数一个默认值(定义函数时, 默认参数一定要放在其他参数的后面, 但是要放在缺省参数的前面)
def greet(name, greetstr="hello there"):
    print("{}, {}".format(greetstr, name))


# 如果形参设置了默认参数, 则在调用方法时, 可以不传该参数(会使用默认参数的值)
greet(name='zzq')

# 如果形参设置了默认参数, 而在调用方法时又传入了该参数, 则会使用传入的值
greet(name='zzq', greetstr='good night')

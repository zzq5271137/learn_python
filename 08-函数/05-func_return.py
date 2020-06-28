"""
函数的返回值
"""


# return语句返回执行结果
def addint(a, b):
    return a + b


print(addint(1, 2))


# 可以返回一个元组(相当于返回了多个值)
# 当然也可以返回其他类型, 比如字典、列表等, 但是使用元组会方便一些, 因为元组具有解组操作, 能够快速获得各个返回值
def greet():
    return 'hello', 'zzq', 100  # 元组的()可以省略(乍一看像是函数返回了多个值, 但其实它是一个元组)


greetstr, name, age = greet()  # 通过解组的方式获取返回值
print("{}, {}, with age {}".format(greetstr, name, age))

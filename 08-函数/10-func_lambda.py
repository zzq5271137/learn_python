"""
Python中的lambda表达式(匿名函数)
"""

# 不使用lambda表达式的方式
people = [
    {
        "name": "zzq",
        "age": 35
    },
    {
        "name": "zhangsan",
        "age": 13
    },
    {
        "name": "lisi",
        "age": 20
    }
]


def my_cmp(x):
    """
    只需要根据age排序
    :param x: 字典
    :return: 字典里的age值
    """
    return x['age']


print("before sort: %s" % people)
people.sort(key=my_cmp)  # 因为只需要根据一个字段进行排序, 所以我们不需要导入和使用cmp_to_key()函数
print("after sort: %s" % people)

print("#######################################################################################")

# 使用lambda表达式的方式
people = [
    {
        "name": "zzq",
        "age": 35
    },
    {
        "name": "zhangsan",
        "age": 13
    },
    {
        "name": "lisi",
        "age": 20
    }
]
print("before sort: %s" % people)
people.sort(key=lambda x: x['age'])  # 匿名函数
print("after sort: %s" % people)

print("#######################################################################################")

"""
Python中的lambda表达式和Java中的lambda表达式不一样;
Python中的lambda表达式只是简单函数(只有一行语句的函数)的简便写法, 它只能有一行语句;
当然, Python中的lambda表达式也是函数式编程思想的一种体现;
几个例子, 如, 传入两个参数并返回他们的和:
    lambda a1, a2: a1 + a2
又如, 无参数只返回一个数字:
    lambda: 100
又如, 还可以使用缺省参数:
    lambda *args, **kwargs: len(args) + len(kwargs)
又如, 和三目运算符组合使用:
    lambda a1, a2: a1 if a1 > a2 else a2
再如, lambda表达式也可以放在列表中, 示例如下
"""
func_list = [lambda x: x.upper(), lambda y: y + 100, lambda x, y: x + y]
print(func_list[0]('abcdefg'))
print(func_list[1](100))
print(func_list[2](1, 2))

print("#######################################################################################")


# lambda表达式可以作为参数传入
def calculate(a, b, cal_func):
    result = cal_func(a, b)
    return result


print(calculate(2, 3, lambda x, y: x + y))
print(calculate(2, 3, lambda x, y: x * y))
print(calculate(2, 3, lambda x, y: x ** y))

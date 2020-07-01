"""
抛出异常与自定义异常
"""


# 抛出异常
def greet(name, age):
    # if type(name) != str:
    if not isinstance(name, str):  # isinstance()方法用于判断某个变量是否是某一类型, 更加方便
        raise ValueError("'name'必须为str类型")  # raise关键字抛出异常
    # if type(age) != int:
    if not isinstance(age, int):
        raise ValueError("'age'必须为int类型")
    print("我叫%s, 年龄是%d" % (name, age))


try:
    greet('zzq', '27')
except ValueError as err:
    print(err.args)

print("######################################################")


# 自定义异常
class ArgumentError(Exception):  # 自定义的异常类, 必须继承自Exception类
    def __init__(self, *args, **kwargs):
        args += ("参数错误",)  # 自定义一些参数, 添加到args元组中(记得*args是一个元组)
        super().__init__(*args, **kwargs)


def greet2(name, age):
    if not isinstance(name, str):
        raise ArgumentError("'name'必须为str类型")  # 抛出自定义的异常
    if not isinstance(age, int):
        raise ArgumentError("'age'必须为int类型")
    print("我叫%s, 年龄是%d" % (name, age))


try:
    greet2('zzq', '27')
except ArgumentError as err:
    print(err.args)

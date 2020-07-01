"""
Python异常处理
"""

"""
try:
    # 可能会抛出异常的代码
except 异常名字:  # 也可以不指定具体异常或者指定的异常为Exception, 表示会catch所有异常
    # try代码块抛出异常后执行的代码
else:
    # try代码块没有抛出异常时执行的代码
finally:
    # 不管try代码块有没有抛出异常, 都会执行的代码
"""

try:
    a = 1
    b = 0
    c = a / b  # ZeroDivisionError
    print("%.2f" % c)
except (ZeroDivisionError, NameError) as err:  # 可以将多个异常写在一个except语句中(元组的形式)
    print('抛出ZeroDivisionError或NameError异常了, 异常信息: {}'.format(err))
except Exception as err:  # 可以写多个except语句
    print("抛出异常了, 异常信息: {}".format(err))
else:
    print('程序运行正常')
finally:
    print('finally...')

print("程序执行结束")

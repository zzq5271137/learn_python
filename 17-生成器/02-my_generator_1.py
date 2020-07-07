"""
自定义生成器
"""

"""
生成器可以通过函数产生; 如果在一个函数中出现了yield表达式, 那么这个函数将不再是一个普通的函数, 而是一个生成器函数,
yield一次返回一个结果, 并且会冻结当前函数的状态, 当下一次外部调用了next()函数或__next__()方法, 
会从上一次冻结的那一行继续往后执行;
"""


def my_generator():  # 和定义函数非常像, 都是使用def关键字
    yield 1  # 碰到yield语句时, 会返回该值, 并且将代码冻结在这里, 当下次再次调用时, 会从下一行继续往下执行
    yield 2
    yield 3


# next()函数可以迭代生成器返回的值, 在调用next()函数时, 会执行我们在定义my_generator()时写的代码
# 其实使用next()函数, 底层还是调用的my_gen的__next__()方法
my_gen = my_generator()  # 注意, 这里返回的不是my_generator()里面的值, 而是返回一个生成器
print('my_gen的类型为: %s' % type(my_gen))  # generator
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

print("###############################################")
# __next__()方法也可以迭代生成器返回的值, 在调用__next__()方法时, 会执行我们在定义my_generator()时写的代码
my_gen = my_generator()
print(my_gen.__next__())
print(my_gen.__next__())
print(my_gen.__next__())

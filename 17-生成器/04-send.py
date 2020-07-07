"""
send()方法
"""

"""
send()函数和next()方法类似, 都可以用来触发生成器的下一个yield; 但是send()函数不仅可以触发下一个yield,
还可以发送数据过去, 作为yield表达式的值(这里的yield表达式的值, 指的是在生成器内部, 如果yield表达式给一个变量赋值,
是这个变量得到的值);
"""


def my_generator(start):
    while start < 10:
        temp = yield start
        print("生成器内部, temp=%s" % temp)
        start += 1


"""
这里会打印如下东西:
外部, current=1
生成器内部, temp=None
外部, current=2

其中第二行, "temp=None"是生成器内部打印的, 但为什么是None呢？不应该是上一次yield返回的值(也就是1)吗？
这是因为, 如果是外部通过next()函数/__next__()方法执行的生成器, yield表达式在内部并不会返回任何值,
(准确的说是只会返回None), 所以, "temp = yield start"这行代码其实是等于"temp = None"的;
"""
my_gen = my_generator(1)
print("外部, 通过next()函数调用, current=%d" % next(my_gen))
print("外部, 通过next()函数调用, current=%d" % next(my_gen))

print("######################################################")

my_gen = my_generator(1)
print("外部, 通过my_gen的send()方法调用, current=%d" % my_gen.send(None))  # send()方法不能在首次调用生成器时传入一个非None值
print("外部, 通过my_gen的send()方法调用, current=%d" % my_gen.send('hello world'))

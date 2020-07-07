"""
案例: 使用yield实现斐波那契数列
"""


def fib(count):
    index = 1
    a, b = 0, 1  # 使用元组的拆组的方式进行赋值
    while index <= count:
        yield b
        temp = b
        b = a + b
        a = temp
        index += 1


my_fib = fib(10)
for x in my_fib:
    print(x, end=' ')
print()

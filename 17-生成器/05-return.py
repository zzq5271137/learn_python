"""
生成器中的return语句会触发StopIterator异常
"""


def my_generator(start):
    while start < 10:
        yield start
        start += 1
        return 'hello world'  # 会触发StopIterator异常


my_gen = my_generator(1)
for x in my_gen:  # 只会打印出1, 因为第一次触发yield后, 下一次会碰到return语句触发StopIterator异常, 从而跳出循环
    print(x)

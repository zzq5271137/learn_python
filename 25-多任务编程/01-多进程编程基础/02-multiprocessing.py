"""
多进程编程: multiprocessing库
"""

from multiprocessing import Process
import time

"""
什么是进程:
操作系统在运行过程中, 一个程序运行起来就是一个进程; 在Python中, 多进程编程可以让我们的程序运行效率更高;

multiprocessing库:
multiprocessing是Python中一个专门用来创建多进程的库, 它提供了一个Process类来创建多进程;
使用multiprocessing库编写的多进程的代码, 是跨平台的, 也就是同一份代码可以在Windows、Linux等操作系统上运行;
(反例是, os模块中有一个fork(), 使用它也可以创建出一个新的进程, 但是这种方法只能在Linux、MacOS操作系统上使用)
以下用一个例子来演示Process类的使用;
"""


def sayhello():
    print('hello world')


if __name__ == '__main__':
    p = Process(target=sayhello)  # 创建一个子进程
    p.start()  # 开启子进程

    while True:
        print('main process running...')
        time.sleep(1)

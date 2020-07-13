"""
with语句魔术方法(会话管理)
"""

"""
with语句魔术方法(会话管理):
Python2.5之后, 定义了一个新的关键字with语句; 之前在讲文件操作的时候, 用过以下代码来打开一个文件以及关闭一个文件:
    with open('xxx.txt', 'r') as fp:
        print(fp.read())
那么, 这种代码的底层原理是什么呢？这种代码专业术语叫做会话控制器, 它通过控制两个魔术方法, __enter__和__exit__,
来定义一个代码块被执行前或者终止后会话管理器应该做什么:
1). __enter__(self)
    只要执行到"with...", 就会自动执行__enter__魔术方法, 并且将__enter__方法的返回值赋值给fp(也就是"as"后面的变量);
2). __exit__(self, exception_type, exception_value, traceback)
    当代码块执行完成之后准备离开的时候, 或者执行代码块时发生了异常, 都会自动执行__exit__方法;
    __exit__可以被用来处理异常、执行一些清除工作或者做一些代码块执行完毕之后的收尾工作;
    如果代码执行成功, 没有异常, 那么exception_type、exception_value、traceback将会是None; 
    否则的话你可以选择处理这个异常或者直接交给用户处理; 如果你想处理这个异常的话, 
    那么必须在__exit__内部执行完成之后返回True(返回False代表__exit__没有处理过异常, 即让用户处理该异常, 即将异常抛出);
    
这里演示模拟一个文件打开器;
"""


class FileOpener(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __enter__(self):
        self.fp = open(*self.args, **self.kwargs)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()
        print('exc_type: %s, exc_val: %s' % (exc_type, exc_val))
        return False


with FileOpener('09-with.txt', 'r') as fp:
    print('文件内容: %s' % fp.read())

    # 模拟异常
    a = 1
    b = 0
    c = a / b

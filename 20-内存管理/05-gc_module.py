"""
gc模块
"""

import gc

"""
Python中的gc模块封装了许多和对象以及垃圾回收相关的方法;
首先, 来回顾一下基础的内容:
1. 导致引用计数+1的情况:
   a. 对象被创建, 并被一个变量所引用, 例如: p1 = Person()
   b. 对象被另一个变量引用, 例如: p2 = p1
   c. 对象被作为参数传递给函数, 例如: func(p1)
   d. 对象被添加到容器中, 比如添加到列表、元组、字典、集合中等, 例如: person_list.append(p1)
2. 导致引用计数-1的情况:
   a. 引用这个对象的变量被删掉了, 例如: del p1
   b. 引用这个对象的变量指向其他对象了
   c. 函数作用域执行完毕后, 比如函数中的一个临时变量, 在这个函数执行结束后就会消失
   d. 对象所在的这个容器被销毁, 或者从容器中删除了这个对象

查看一个对象的引用计数, 使用sys.getrefcount(), 例如:
    import sys
    a = 'zzq'
    print(sys.getrefcount(a))
使用sys.getrefcount()获取的引用计数总是会多1, 因为你将这个对象传递给了getrefcount()函数, 
这个过程会给对象的引用计数+1
"""

"""
gc模块常用函数:
1. gc.set_debug(flags):
   启用gc的debug日志, flags一般设置为gc.DEBUG_LEAK, 可以看到内存泄漏的对象
2. gc.collect(generation):
   手动执行垃圾回收; 会将那些有循环引用的对象给回收了(即手动触发一次某些代链表的遍历);
   这个函数可以传递参数, generation, 代表回收某些代链表的垃圾对象,
   例如, 传入0代表回收第0代的垃圾对象, 1代表回收第0代和第1代的垃圾对象,
   2代表回收第0、1、2代的垃圾对象; 如果不传参数, 那么默认generation为2;
   当达到各代链表各自的阈值时, Python就会自动调用gc.collect()函数;
   当然你也可以手动调用gc.collect()函数, 手动地进行垃圾回收;
3. gc.get_threshold():
   获取gc模块执行垃圾回收的阈值; 返回一个元组, 元组中下标为i的元素代表第i代的阈值;
4. gc.set_threshold():
   设置执行垃圾回收的阈值
5. gc.get_count():
   获取当前自动执行垃圾回收的计数器; 返回一个元组, 元组中下标为0的元素代表第0代的垃圾对象的数量,
   下标为1的元素代表第0代链表的遍历次数, 下标为2的元素代表第1代链表的遍历次数;
   
注: 一共就只有零代链表、一代链表、二代链表这3个链表
"""

print('阈值: {}'.format(gc.get_threshold()))
gc.set_threshold(100)
print('阈值: {}'.format(gc.get_threshold()))
print('计数: {}'.format(gc.get_count()))
gc.set_debug(gc.DEBUG_LEAK)

print("################################################")


class Person(object):
    def __init__(self, name):
        self.name = name
        self.pointer = None

    def __del__(self):
        print("%s执行了del函数" % self.name)


while True:
    print('计数: {}'.format(gc.get_count()))
    p1 = Person('p1')
    p2 = Person('p2')
    p1.pointer = p2
    p2.pointer = p1
    del p1
    del p2
    gc.collect()
    a = input('test: ')

"""
自定义生成器
"""


def my_generator(start, end):
    current = start
    while current <= end:
        yield current
        current += 1


my_gen = my_generator(1, 10)  # 注意, 这里返回的不是my_generator()里面的值, 而是返回一个生成器
print('my_gen的类型为: %s' % type(my_gen))  # generator

"""
还记得16-迭代器/03-my_iterable_iterator_1.py中讲到的for循环原理:
当执行"for x in Iterable对象"时, 会通过该Iterable对象的__iter__()方法拿到迭代器对象,
拿到迭代器对象后, 在每次循环中, 会调用该迭代器对象的__next__()方法去获取值, 并赋值给x, 
然后你就可以在循环体内使用x了; 当调用__next__()方法抛出StopIteration异常时, 会退出循环;

在这里, for循环每次遍历时也是会调用__next__()方法, 由于生成器本身也是属于可迭代的对象, 也是属于迭代器对象,
并且__next__()方法可以迭代生成器的返回值, 所以使用for循环可以正常地遍历生成器(在调用__next__()方法时,
会执行我们在定义my_generator()时写的代码);
"""
print("第一次迭代")
for x in my_gen:
    print(x, end=' ')
print()

print("#############################################################################")

"""
因为生成器集合了可迭代对象和迭代器对象两个身份, 所以一个生成器对象只能被for循环迭代一次(因为它没有重置状态)
"""
print("第二次迭代")
for x in my_gen:
    print(x, end=' ')
print()

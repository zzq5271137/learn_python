"""
可变的数据类型
"""

# 列表和字典都是可变的数据类型, 因为你可以对里面的内容进行增删改; 对于诸如列表、字典这种可变的数据类型,
# 当把他们用作全局变量, 在函数或者代码块中使用的时候, 可以任意地直接增删改里面的值, 不需要使用global关键字
# (有点像Java中的栈和堆的关系, people变量存在栈中, 真正的对象存在堆中, 栈中的变量指向堆中的内容)
people = ['zhangsan', 'lisi']


def func1():
    people.append('zzq')  # 只是修改里面的内容, 不需要global


print("before call func1: %s" % str(people))
func1()
print("after call func1: %s" % str(people))


# 但是如果要修改它的指向(给变量重新赋值), 则需要加上global关键字; 如果不加global关键字, 则代表创建了一个本地变量
def func2():
    global people
    people = ['the', 'world']  # 修改地址指向(给变量重新赋值), 需要global


print("before call func2: %s" % str(people))
func2()
print("after call func2: %s" % str(people))

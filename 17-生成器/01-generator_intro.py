"""
生成器(generator)
"""

"""
为什么需要生成器:
假如现在有一个需求, 是打印从一到一亿的整数, 如果我们采用range()函数并将其返回的结果放入一个变量中的方式, 那么程序肯定会崩溃,
因为range(1, 100000000)会直接产生一个从1到100000000的列表, 这个列表中的所有数据都是存放在内存中的,
就会直接导致内存爆满; 这时候, 我们就可以采用生成器来解决这个问题, 生成器不会一次性地把所有数据加载到内存中,
而是在循环的时候临时生成数据, 循环一次生成一个, 所以在程序运行期间永远都只会生成一个数据, 从而大大节省内存;
"""

# 使用生成器的第一种方式: 在使用列表生成式时, 使用圆括号代替列表生成式的方括号, 从而产生一个生成器
num_list = [x for x in range(1, 11)]  # 普通的列表(使用列表生成式产生一个列表)
print(type(num_list))
num_generator = (x for x in range(1, 11))  # 使用圆括号的方式可以产生一个生成器(这是一个语法, 牢记)
print(type(num_generator))

# 生成器本身也是属于可迭代的对象, 也是属于迭代器对象, 所以可以通过for循环进行遍历
for x in num_generator:
    print(x, end=' ')
print()

# 使用生成器的第二种方式: 自己定义生成器, 详见: 02-my_generator.py

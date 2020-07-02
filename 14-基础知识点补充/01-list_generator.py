"""
列表生成式
"""

"""
列表生成式, 是用于生成列表的简写形式, 可以将好几行的代码写在一行中
"""

# 比如要获取一个从1~10的整数值的列表, 如果使用传统的方式, 会这么写:
values_1 = []
for x in range(1, 11):  # 记得range()左闭右开
    values_1.append(x)
print(values_1)

# 如果使用列表生成式, 那么可以通过以下一行代码实现:
values_2 = [x for x in range(1, 11)]
print(values_2)

# 当然也可以在写列表生成式的时候添加条件, 只有满足条件的才会被加到列表中:
values_3 = [x for x in range(1, 11) if x % 2 == 0]  # 生成一个范围为1~10的偶数列表
print(values_3)

# 生成式中后面的"for x in range(1, 11)"只是为了控制循环的, 表示生成的列表有几个元素, 这其中的x是一个变量,
# 它可以在最前面处被使用, 也可以在后面的if中被使用, 具体生成的列表是什么样, 主要是看最前面的"x"写成什么样;
# 所以, 还可以更加花式地生成列表:
values_4 = [x ** 2 for x in range(1, 11) if x % 2 != 0]  # 取出1~10的奇数, 将每个数的平方生成一个列表
print(values_4)
# 或者:
values_5 = ['zzq' for x in range(1, 11)]  # 含有10个'zzq'的列表
print(values_5)

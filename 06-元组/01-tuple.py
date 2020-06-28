"""
元组:
元组的使用与列表相似, 不同之处在于元组是不可修改的, 一个元组一旦定义了, 就不可修改了(不可添加、删除元素等), 只能遍历/访问;
元组使用圆括号, 而列表使用方括号;
既然元组不能够修改, 那么它存在的意义在哪呢:
1. 元组在字典中可以当做key来使用, 而列表是不可以的;
2. 在函数中, 有时候要返回多个值, 一般就采用元组的方式;
3. 在一些不希望用户修改数据的场景中使用元组代替列表;
元组的数据类型是: tuple
"""

# 定义元组: 使用逗号的方式
print("定义元组: 使用逗号的方式")
tuple1 = 1, 2, 3
print(tuple1)
print(type(tuple1))

print("#################################################")

# 定义元组: 使用圆括号的方式
print("定义元组: 使用圆括号的方式")
tuple2 = (1, 2, 3)
print(tuple2)
print(type(tuple2))

print("#################################################")

# 定义元组: 使用tuple()函数(接收一个列表作为参数)
print("定义元组: 使用tuple()函数(接收一个列表作为参数)")
list1 = [1, 2, 3]
tuple3 = tuple(list1)
print(tuple3)
print(type(tuple3))

print("#################################################")

# 定义只有一个元素的元组
print("定义只有一个元素的元组")
aTuple = 'a',  # 必须要加逗号
print(aTuple)
print(type(aTuple))
bTuple = ('b',)  # 必须要加逗号
print(bTuple)
print(type(bTuple))

print("#################################################")

# 与列表一样, 一个元组中也可以包含多种类型的数据
tuple4 = (1, 'a', True)
print(tuple4)
tuple5 = (1, ['a', 'b'], (2, 'c', 5.5))  # 嵌套
print(tuple5)

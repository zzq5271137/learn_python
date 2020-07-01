"""
元组常用操作
"""

# 下标操作
print("下标操作")
tuple1 = ('zzq', 100)
print("name is %s, age is %d." % (tuple1[0], tuple1[1]))

print("#####################################################")

# 切片操作: 和字符串的切片操作是一样的, 详见04-字符串/05-str_slice.py
print("切片操作")
tuple2 = (0, 1, 2, 3, 4, 5)
tuple2_slice = tuple2[-1::-1]
print(tuple2_slice)

print("#####################################################")

# 解组操作
print("解组操作")
tuple3 = ('zzq', 100, 'Shanghai')
name, age, address = tuple3  # 当然也可以用下标操作一个一个地取出来, 但是解组操作会更方便简洁一些(要注意元素个数和顺序)
print("name is %s, age is %d, address is %s." % (name, age, address))
tuple4 = ('Math', 'English', 'Science', 'Art')
subject1, _, _, subject2 = tuple4  # 有些时候我们只需要元组中的某个或某些值, 则剩下的值可以用"_"来占位(要注意元素个数和顺序)
print("Subjects are: %s, %s." % (subject1, subject2))

print("#####################################################")

# 相加操作
print("相加操作")
tuplea = (1, 2)
tupleb = (3, 4)
tuplec = tuplea + tupleb
print(tuplec)

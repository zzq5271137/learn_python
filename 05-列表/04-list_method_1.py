"""
列表常用方法
"""

# append(): 在列表末尾添加元素(会改变原列表)
# 注: 与Java中的数组不同, Java中的数组一旦定义了, 长度就不可变了, 而Python中的列表的长度是可变的
print("append()")
list1 = [1, 2, 3]
print("before append: %s" % str(list1))
list1.append(4)
print("after append: %s" % str(list1))

print("###############################################3")

# count(): 统计某个元素在列表中出现的次数
print("count()")
list2 = [1, 2, 3, 1, 2, 5, 7, 1]
print(list2.count(1))

print("###############################################3")

# extend(): 将一个列表的内容追加到另一个列表的后面(会改变原列表)
# 使用extend()和使用列表相加操作的区别在于, 使用列表相加操作, 不会改变原有列表的值, 而是会生成一个新的列表,
# 而使用extend()会改变原有列表的值(直接在原有列表的后边追加内容)
print("extend()")
lista = [1, 2, 3]
print("before extend: %s" % str(lista))
lista.extend([4, 5, 6])
print("after extend: %s" % str(lista))

print("###############################################3")

# index(): 找出某元素(传入的参数)在列表中第一次出现的位置, 没有找到则抛出异常
print("index()")
list3 = ['zzq', 'the', 'world']
print(list3.index('world'))

print("###############################################3")

# insert(): 将某个值插入到列表中的某个位置(如果插入的位置不是末尾, 则相应位置及其后面位置的元素会往后平移)
print("insert()")
list4 = ['zzq', 'the', 'world']
print("before insert: %s" % str(list4))
list4.insert(1, 'zzq2')
print("after insert at index 1: %s" % str(list4))

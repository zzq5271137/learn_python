"""
列表常用方法
"""

# pop(): 移除列表中的最后一个元素, 并返回该元素的值
print("pop()")
list1 = [1, 2, 3, 4, 5]
print("before pop: %s" % str(list1))
list1_pop = list1.pop()
print("after pop: %s, the value of the popped element: %d" % (str(list1), list1_pop))

print("#######################################################")

# remove(): 移除列表中第一个匹配的元素(传入的参数), 不会返回这个被移除的元素的值; 如果找不到这个元素, 则会抛出异常
print("remove()")
list2 = [1, 2, 3, 4, 5, 3]
print("before remove: %s" % str(list2))
list2.remove(3)
print("after remove element 3: %s" % str(list2))

print("#######################################################")

# reverse(): 将列表中的元素反向存储, 会改变原有列表
# reverse()方法与通过列表的切片操作进行逆序(list[-1::-1])的区别在于, 切片操作会生成一个新的列表, 原有列表不会改变,
# 而reverse()方法是直接将原有列表进行逆序存储, 会改变原有列表
print("reverse()")
list3 = [1, 2, 3, 4, 5]
print("before reverse: %s" % str(list3))
list3.reverse()
print("after reverse: %s" % list3)

print("#######################################################")

# sort(): 将列表中的元素进行排序, 会改变原有列表
print("sort()")
list4 = [3, 6, 2, 4, 1, 5]
print("before sort: {}".format(str(list4)))
# list4.sort()  # 默认升序
list4.sort(reverse=True)  # 降序排序
print("after sort: {}".format(str(list4)))
print("#######################################################")
# 要区分sort()方法与sorted()函数, sort()方法是由一个列表去调用的, 它会改变原有列表;
# sorted()函数是直接调用的(传入一个列表作为参数), 它不会改变原有列表, 而是会生成一个新的列表
print("sorted()")
list5 = [3, 6, 2, 4, 1, 5]
print("before sorted: list5={origin}".format(origin=str(list5)))
list5_sorted = sorted(list5)
print("after sorted: list5={origin}, list5_sorted={sorted}".format(origin=str(list5),
                                                                   sorted=str(list5_sorted)))

print("#######################################################")

# del关键字: 根据下标删除列表元素
print("del关键字")
list6 = [0, 1, 2, 3, 4, 5]
print("before del: %s" % str(list6))
del list6[3]
print("after del element at index 3: %s" % str(list6))

print("#######################################################")

# in关键字: 判断列表中是否有某个元素
print("in关键字")
list7 = [1, 2, 3, 4, 5]
print("列表: %s" % str(list7))
print("列表中是否有元素3: %s" % (3 in list7))

print("#######################################################")

# list(): 将其他数据类型转换成列表(list), 参数必须是一个可以迭代的对象(Iterable)
print("list()")
list8 = list('abcde')
print(list8)
print(type(list8))

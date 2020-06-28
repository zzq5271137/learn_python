"""
列表的基本操作
"""

# 列表嵌套: 和Java的数组不同, Python中的一个列表中可以存储任何的数据类型, 甚至列表中可以存储列表, 即列表的嵌套
print("列表嵌套")
list1 = ['hello', 37, ['zzq', 100]]
for element in list1:
    print(element)

print("####################################################")

# 列表相加: 相当于把后面一个列表的内容追加到前面一个列表后面
print("列表相加")
lista = [1, 2, 3]
listb = [4, 5, 6]
listc = lista + listb
print(listc)

print("####################################################")

# 列表的切片操作: 和字符串的切片操作是一样的, 详见04-字符串/05-str_slice.py
print("列表的切片操作")
# 小案例: 将列表进行逆序操作
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_num_reverse = list_num[-1::-1]
print(list_num)
print(list_num_reverse)

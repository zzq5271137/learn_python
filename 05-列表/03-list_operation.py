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

print("####################################################")

# 列表的解组操作: 和元组的解组操作非常像
print("列表的解组操作")
student_attr = ['zzq', 27, '820064']
print('student_attr = %s' % student_attr)
student_name, student_age, student_id = student_attr
print('学生姓名: %s, 学生年龄: %d, 学生学号: %s' % (student_name, student_age, student_id))

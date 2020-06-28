"""
字典常用方法
"""

# clear(): 清除字典中的所有项
print("clear()")
dict1 = {"username": "zzq", "age": 100, "dob": "1993-06-03"}
print("before clear: %s" % str(dict1))
dict1.clear()
print("after clear: %s" % str(dict1))
print("##################################################################")
# 使用clear()方法清空字典与直接将变量重新赋值为空字典的区别
# 可以发现, 使用clear()方法, 是直接将内存中的内容进行清空, 所以在clear()了dict1后,
# dict1_copy也为空了, 因为dict1和dict1_copy指向的是同一块内存空间;
# 而直接将变量dict1重新赋值为{}, 是将dict1指向一块新的内存空间, 而原来的那块内存空间中的内容并没有改变
# 并且dict1_copy的指向也没有改变, 所以在重新赋值dict1后, dict1_copy并没有改变
print("使用clear()方法清空字典与直接将变量重新赋值为空字典的区别")
dict1 = {"username": "zzq", "age": 100, "dob": "1993-06-03"}
dict1_copy = dict1
# dict1.clear()
dict1 = {}
print(dict1_copy)

print("##################################################################")

# get(): 根据key(传入的参数)取值; 与使用字典的下标操作来取值的区别在于, 当key不存在时, get()不会抛出异常
print("get()")
dict2 = {"username": "zzq", "age": 100, "dob": "1993-06-03"}
print(dict2.get("username"))
print(dict2.get("city"))  # 因为此key不存在, 所以取到的是None
print(dict2.get("city", "Shanghai"))  # 也可以指定一个, 在没有获取到值时的默认值

print("##################################################################")

# pop(): 获取给定key(传入的参数)的值, 然后将这个键值对从字典中删除
print("pop()")
dict3 = {"username": "zzq", "age": 100, "dob": "1993-06-03"}
print("before pop: %s" % str(dict3))
username = dict3.pop("username")
print("after pop with key username: %s, the popped value: %s" % (dict3, username))

print("##################################################################")

# popitem(): 随机从字典中取出一个键值对, 然后删除该键值对(因为字典是无序的, 所以popitem()是随机的)
print("popitem()")
dict4 = {"username": "zzq", "age": 100, "dob": "1993-06-03"}
print("before popitem: %s" % str(dict4))
item = dict4.popitem()  # 会返回一个二元元组, (key, value)
print("after popitem: %s, the popped value: %s" % (str(dict4), item))

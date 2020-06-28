"""
字典的基本操作
"""

# len(): 获取字典的键值对的长度(有多少个键值对)
dict1 = {"username": "zzq1", "age": 100, "dob": "1993-06-03"}
print(len(dict1))

print("##############################################################")

# 下标操作, 根据key取value, 如果key不存在, 会抛出异常(使用get()方法不会抛出异常)
print("name is %s, age is %d, birthday is %s" % (dict1["username"], dict1["age"], dict1["dob"]))

print("##############################################################")

# 修改value/添加新的键值对
dict2 = dict(k1="v1", k2="v2", k3="v3")
print("before change: %s" % str(dict2))
dict2['k2'] = 'v2_new'
dict2['k4'] = 'v4_added'  # 如果这个key在原有字典中并不存在, 则会向该字典中添加
print("after change: %s" % str(dict2))

print("##############################################################")

# 使用del关键字删除键值对
dict3 = dict(k1="v1", k2="v2", k3="v3")
print("before del: %s" % str(dict3))
del dict3["k2"]
print("after del with key k2: %s" % str(dict3))

print("##############################################################")

# 使用in关键字检查字典是否包含某一个key
dict4 = dict(k1="v1", k2="v2", k3="v3")
print("是否包含key为k2的键值对: %s" % ("k2" in dict4))

print("##############################################################")

# 字典中的key可以是任意的不可变类型, 比如: 整型、字符串、浮点类型、元组
dict5 = {"a": "a", 1: "b", 1.2: "c", (7, 'x'): ("d",), (8, 'z'): ['e', 'f', 'g']}
print(dict5)

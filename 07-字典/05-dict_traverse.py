"""
字典的遍历
"""

# keys(): 将字典中所有的键以列表的形式返回
print("keys()")
dict1 = {"k1": "v1", "k2": "v2", "k3": "v3"}
dict1_keys = dict1.keys()
print(dict1_keys)
for k in dict1_keys:
    print("{}={}".format(k, dict1[k]))

print("###########################################################")

# values(): 将字典中所有的值以列表的形式返回
print("values()")
dict1_values = dict1.values()
print(dict1_values)
for v in dict1_values:
    print(v)

print("###########################################################")

# items(): 将字典中所有的键值对以列表的形式返回(二元元组的列表)
print("items()")
dict1_items = dict1.items()
print(dict1_items)
# for item in dict1_items:
#     print("{}={}".format(item[0], item[1]))
for key, value in dict1_items:  # 使用元组解组操作, 更方便
    print("{}={}".format(key, value))

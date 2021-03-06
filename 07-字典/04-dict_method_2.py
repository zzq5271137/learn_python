"""
字典常用方法
"""

# update(): 用一个字典更新另外一个字典(将第二个字典的内容追加到第一个字典中, 如果碰到相同的键, 则会覆盖)
print("update()")
dicta = {"name": "zzq1", "url": "www.baidu.com"}
print("before update: %s" % str(dicta))
dictb = {"name": "zzq2", "age": 20}
dicta.update(dictb)
print("after update: %s" % str(dicta))

print("#####################################################")

# setdefault(): 传入一个键和一个值, 如果字典中包含给定键, 则返回该键对应的值, 否则将该键值对设置到字典中(并返回设置的值)
print("setdefault()")
dict1 = {"name": "zzq1", "url": "www.baidu.com"}
print("before setdefault: %s" % str(dict1))
val = dict1.setdefault("gender", 'male')
print("after setdefault: %s, the value: %s" % (str(dict1), val))

print("#####################################################")

# items(): 以列表返回可遍历的(key, value)二元元组数组
print("items()")
dict2 = {"name": "zzq1", "age": 27, "url": "www.baidu.com"}
for entry in dict2.items():  # 以元组的下标的形式进行遍历
    print('%s=%s' % (entry[0], entry[1]), end=', ')
print()
for key, value in dict2.items():  # 以元组的解组的形式进行遍历
    print('%s=%s' % (key, value), end=', ')
print()

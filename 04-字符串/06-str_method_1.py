"""
字符串常用方法
"""

# find(): 从一个字符串中查找一个子串, 如果找到了, 返回这个子串在字符串中开始的位置, 如果找不到, 返回-1; rfind()是从右边开始查找
print("find()和rfind()")
str1 = "hello world world"
position = str1.find("world")
print(position)
position = str1.rfind("world")
print(position)

print("####################################")

# index(): 和find()非常类似, 只不过当找不到这个子串时会抛出异常而不是返回-1; rindex()是从右边开始查找
print("index()和rindex()")
position = str1.index("world")
print(position)
position = str1.rindex("world")
print(position)

print("####################################")

# len(): 获取字符串的长度
print("len()")
print(len(str1))

print("####################################")

# count(): 获取子串在原字符串中出现的次数
print("count()")
print(str1.count("world"))

print("####################################")

# replace(): 创建一个新的字符串, 把原字符串中某个子串替换为你想要的子串(不会改变原来字符串的值)
print("replace()")
str2 = str1.replace("world", "world2")
print(str1)
print(str2)

print("####################################")

# split(): 按照给定的字符串将一个字符串进行分割, 返回一个列表
print("split()")
strList = str1.split(" ")
print(strList)
print(type(strList))  # list

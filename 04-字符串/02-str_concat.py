"""
字符串的拼接
"""

# 使用"+"进行拼接
str1 = "hello "
str2 = "world"
str3 = str1 + str2
print(str3)

print("########################################")

# 使用格式化的方式拼接, %s: 代表字符串的占位符, %d: 代表整型的占位符, %f: 代表浮点类型的占位符
name = "zzq"
age = 100
greet = "My name is %s, and my age is %d." % (name, age)
print(greet)

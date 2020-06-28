"""
字符串常用方法
"""

# startswith(): 判断某字符串是否是以某子串(传入的参数)开头的, 这个子串不需要是完整的单词
print("startswith()")
str1 = "hello world"
print(str1.startswith("hello"))

print("##################################################")

# endswith(): 判断某字符串是否是以某子串(传入的参数)结尾的, 这个子串不需要是完整的单词
print("endswith()")
print(str1.endswith("world"))

print("##################################################")

# lower(): 将字符串全部改成小写(会返回一个新的字符串, 原来的字符串不变)
print("lower()")
str2 = "aBcDEFg"
str2_lower = str2.lower()
print(str2)
print(str2_lower)

print("##################################################")

# upper(): 将字符串全部改成大写(会返回一个新的字符串, 原来的字符串不变)
print("upper()")
str2_upper = str2.upper()
print(str2)
print(str2_upper)

print("##################################################")

# strip(): 将字符串左右的空格都删掉(会返回一个新的字符串, 原来的字符串不变)
print("strip()")
str3 = " zzq "
str3_all_strip = str3.strip()
print(str3)
print(str3_all_strip)

print("##################################################")

# lstrip(): 删除字符串左边的空格(会返回一个新的字符串, 原来的字符串不变)
print("lstrip()")
str3_left_strip = str3.lstrip()
print(str3)
print(str3_left_strip)

print("##################################################")

# rstrip(): 删除字符串左边的空格(会返回一个新的字符串, 原来的字符串不变)
print("rstrip()")
str3_right_strip = str3.rstrip()
print(str3)
print(str3_right_strip)

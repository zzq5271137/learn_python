"""
字符串常用方法
"""

# partition(): 传入一个str参数, 从str出现的第一个位置起, 把字符串string分成一个3元素的元组(tuple),
# (string_pre_str, str, string_post_str), 如果string中不包含str, 则string_pre_str == string,
# 然后剩下的str和string_post_str为空字符串
print("partition()")
str1 = "HelloZzqPython"
str1_partition = str1.partition("Zzq")
print(str1)
print(str1_partition)
print(type(str1_partition))

print("#################################################")

# isalnum(): 如果string至少有一个字符且所有字符都是字母或数字, 则返回True, 否则返回False
print("isalnum()")
str2 = "abc123"
print(str2.isalnum())

print("#################################################")

# isalpha(): 如果string至少有一个字符且所有字符都是字母, 则返回True, 否则返回False
print("isalpha()")
str3 = "abc"
print(str3.isalpha())

print("#################################################")

# isdigit(): 如果string至少有一个字符且所有字符都是数字, 则返回True, 否则返回False
print("isdigit()")
str4 = "123"
print(str4.isdigit())

print("#################################################")

# isspace(): 如果string只包含空格, 则返回True, 否则返回False
print("isspace()")
str5 = "   "
print(str5.isspace())

print("#################################################")

# format(): 格式化字符串, 详见: 03-str_format.py
print("format()")
name = "zzq"
age = 100
score = 90.37
# 方式一, 使用位置参数占位符(填参数时要按顺序):
greet = "My name is {}, my age is {}, and my score is {}.".format(name, age, score)
print(greet)
# 方式二, 使用关键字参数占位符(填参数时顺序可以乱):
greet = "My name is {arg1}, my age is {arg2}, and my score is {arg3}.".format(arg3=score, arg1=name,
                                                                              arg2=age)
print(greet)

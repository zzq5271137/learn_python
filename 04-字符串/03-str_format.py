"""
字符串的格式化
"""

# 使用"%"进行格式化, %s: 代表字符串的占位符, %d: 代表整型的占位符, %f: 代表浮点类型的占位符
name = "zzq"
age = 100
score = 90.37
greet = "My name is %s, my age is %d, and my score is %.1f." % (name, age, score)
print(greet)

print("##############################################")

# 使用format()方法(str类型的实例方法)进行格式化
# 方式一, 使用位置参数占位符(填参数时要按顺序):
greet = "My name is {}, my age is {}, and my score is {}.".format(name, age, score)
print(greet)
# 方式二, 使用关键字参数占位符(填参数时顺序可以乱):
greet = "My name is {arg1}, my age is {arg2}, and my score is {arg3}.".format(arg3=score, arg1=name,
                                                                              arg2=age)
print(greet)

print("##############################################")

# 使用 f-string
greet = f'My name is {name}, my age is {age}, and my score is {score}'
print(greet)

"""
数据类型的转换
"""

# 浮点类型转换为整型
print("浮点类型转换为整型")
a = 4.9
b = int(a)  # 直接舍弃掉小数部分, 不会四舍五入
print(b)
print(type(b))

print("###############")

# 将字符串类型转换为整型
print("将字符串类型转换为整型")
c = "123"
d = int(c)  # int()函数规定字符串不可以包含非数字的字符, 所以不可以转换浮点类型的字符串(想要转换浮点类型的字符串, 使用float()函数)
print(d)
print(type(d))

print("###############")

# 将整型/浮点类型转换为字符串
print("将整型/浮点类型转换为字符串")
e = 123
e_str = str(e)
print(e_str)
print(type(e_str))
f = 123.9
f_str = str(f)
print(f_str)
print(type(f_str))

print("###############")

# 将整型转换为浮点类型
print("将整型转换为浮点类型")
g = 2
h = float(g)
print(h)
print(type(h))

print("###############")

# 将字符串转换为浮点类型
print("将字符串转换为浮点类型")
i = "123.9"
j = float(i)
print(j)
print(type(j))

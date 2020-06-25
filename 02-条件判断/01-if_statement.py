"""
条件判断语句if
"""

# 布尔类型
y = True
z = False
print(y)
print(type(y))  # bool
print(z)
print(type(z))  # bool

print("###########################")

# ==
a = 1
b = 2
if a == b:
    print("a和b相等")
else:
    print("a和b不相等")

print("###########################")

# 只有数据类型是一样的, 才可以进行判断, 否则直接是False
c = 1
d = "1"
print(c == d)

print("###########################")

# and
if a == 1 and b == 2:
    print("合格！")
else:
    print("不合格")

print("###########################")

# or
age = int(input("请输入年龄: "))
if age < 15 or age > 24:
    print("您不是青年人")
else:
    print("您是青年人")

print("###########################")

# not
if not a > 0:
    print("a不是正数")
else:
    print("a是正数")

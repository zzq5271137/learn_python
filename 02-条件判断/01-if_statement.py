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

"""
关于Python中的代码块:
Python是一个对缩进很严格的语言, Python中的代码块是由缩进决定的;
例如上面的if语句代码块, 只有处于if语句之下并且带有缩进形式(相较于if语句进行缩进)的语句才属于该if语句代码块中, 
直到碰到一条与if语句平级(不带缩进)的语句, 表示退出了该if语句的代码块(该条语句不属于该if语句的代码块);
其他的代码块也是这样, 比如while、for等循环语句的代码块, 自定义函数的代码块, with语句代码块等;
"""

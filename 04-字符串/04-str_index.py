"""
字符串的下标操作
"""

# 在Python中, 一个字符串中的字符可以通过下标取出来(下标从0开始)
name = "abcde"
index = 0
while index < len(name):
    print(name[index])
    index += 1

print("##############################")

# 下标如果是正数, 是从左往右数然后获取字符(从0开始, 然后1、2、3...)
# 下标如果是负数, 是从右往左数然后获取字符(从-1开始, 然后-2、-3、-4...)
index = -1
while abs(index) <= len(name):
    print(name[index])
    index -= 1

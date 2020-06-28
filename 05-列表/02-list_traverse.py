"""
列表的遍历
"""

# 使用while循环遍历列表
fruites = ['apple', 'banana', 'orange']
index = 0  # 列表的下标从0开始
while index < len(fruites):
    print("%d=%s" % (index, fruites[index]), end=" ")
    index += 1
print()

print("#########################################################")

# 使用for循环遍历列表
whatever = ['a', True, 1, 2.3]
for element in whatever:
    print(element, end=" ")
print()

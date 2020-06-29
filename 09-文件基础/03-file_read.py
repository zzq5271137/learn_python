"""
文件读取的三种方式
"""

# read()函数: 读取文件的全部内容
fp = open("03-file_read.txt", 'r')
content = fp.read()
print(content)
fp.close()

print("########################################################")

# read()函数: 也可以读取指定个字节(传入的参数)
fp = open("03-file_read.txt", 'r')
content = fp.read(5)
print(content)
fp.close()

print("########################################################")

# readline()函数: 读取一行数据, 没调用一次, 指针就往下移动一行
fp = open("03-file_read.txt", 'r')
print("第一次读取: %s" % fp.readline(), end="")
print("第二次读取: %s" % fp.readline(), end="")
print("第三次读取: %s" % fp.readline(), end="")
print()
fp.close()

print("########################################################")

# 使用readline()函数, 遍历文件中的所有内容
fp = open("03-file_read.txt", 'r')
while True:
    content = fp.readline()
    if not content:
        break
    print(content, end="")
print()
fp.close()

print("########################################################")

# readlines()函数: 将文件中所有的内容读出来放到一个列表中(列表中的每一个元素代表文件中的一行内容)
# readlines()函数有一个注意点, 读取出的文件内容都是放在内存中的, 如果这个文件比较大,
# 那么readlines()函数把这所有内容都放在内存中, 会对内存造成很大的压力, 甚至可能会造成内存溢出;
fp = open("03-file_read.txt", 'r')
alllines = fp.readlines()
print(alllines)
fp.close()

print("########################################################")

# 遍历文件指针对象(推荐)
# 使用这种方式有几个好处, 一个是写法简洁明了, 另一个是它不会像readlines()一样一次将所有内容都读出来, 所以不会对内存造成太大压力
fp = open("03-file_read.txt", 'r')
for line in fp:  # 文件指针对象是一个可迭代的对象, 所以可以直接迭代它
    print(line, end="")
print()
fp.close()

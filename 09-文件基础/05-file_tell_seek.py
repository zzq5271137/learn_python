"""
文件指针的定位操作
"""

# tell(): 文件指针, 相当于你打开该文件时的光标位置; 对文件指针对象(fp)的所有操作(读、写等), 都是基于文件指针的位置的;
# 可以通过tell()方法来获取文件指针的当前位置;
fp = open("05-file_tell_seek.txt", 'r', encoding='utf-8')
position = fp.tell()
print("'r'方式打开文件, 默认文件指针开始的位置: {}".format(position))
content = fp.read(3)  # 读取3个字节
position = fp.tell()
print("读取到的内容: {}, 当前文件指针所在位置: {}".format(content, position))
content = fp.read(3)  # 读取3个字节
position = fp.tell()
print("读取到的内容: {}, 当前文件指针所在位置: {}".format(content, position))
fp.close()

print("###########################################################################")

# seek(): seek()方法可以将文件指针定位到某一个位置;
# 例如, 我们在读写文件的过程中, 需要从另外一个位置进行操作, 就可以使用seek();
# seek(offset, from)有两个参数, offset代表偏移量, from代表相对位置;
# from相对位置参数: "0"表示从文件开头, "1"表示从当前位置, "2"表示从文件末尾;
# 在Python3中, 如果from的值不是0, 那么offset就必须为0;

# demo1: 将文件指针定位到, 离文件开头位置偏移6个字符的地方
print("demo1:")
fp = open("05-file_tell_seek.txt", 'r', encoding='utf-8')
fp.seek(6, 0)  # 将文件指针定位到, 离文件开头位置偏移6个字符的地方
content = fp.read(5)
print(content)
fp.close()

# demo2: 将文件指针定位到, 离文件末尾位置偏移5个字符的地方
print("demo2:")
fp = open("05-file_tell_seek.txt", 'r', encoding='utf-8')
fp.seek(0, 2)  # 先把文件指针移动到文件末尾
end = fp.tell()  # 获取当前位置(文件末尾位置)
fp.seek(end - 5, 0)  # 将文件指针定位到, 离文件末尾位置偏移5个字符的地方
content = fp.read(3)
print(content)
fp.close()

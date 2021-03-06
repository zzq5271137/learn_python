"""
文件的打开方式
"""

# read()方法
fp = open("02-file_open_mode.txt", 'r')
content = fp.read()
print(content)
fp.close()

# write()方法
fp = open("02-file_open_mode.txt", 'a')
fp.write('\ntoday is sunday')
fp.close()

# Python2和Python3默认打开文件的编码
# Python2操作文件时, 默认使用的是utf-8编码;
# Python3操作文件时, 默认使用的是你操作系统自带的编码;
# 如果想要在Python3中操作文件时使用utf-8编码, 需要在open()函数中传入encoding='utf-8'参数;
fp = open("02-file_open_mode.txt", 'a', encoding='utf-8')
fp.write('\n你好世界')
fp.close()

print("#####################################################################")

# r: 读的方式打开文件, 不能用于写入;

# w: 写的方式打开文件, 不能用于读取;
# 'w'的方式打开文件, 如果这个文件已存在, 则会删掉并重新创建; 如果这个文件不存在, 则会创建这个文件;

# a: 追加的方式打开文件, 不能用于读取;
# 'a'的方式打开文件, 其写入的内容会追加到原来文件的内容后面, 不会覆盖;

# r+: 读写的方式打开文件;
# r+拥有r的基因, 即文件指针是在文件最开始的地方, 所以如果去写的话, 会在文件开头添加内容, 而且会替换掉与写入长度相同的原内容;

# w+: 读写的方式打开文件;
# w+拥有w的基因, 即如果这个文件不存在, 则会创建这个文件; 如果这个文件已存在, 则会删掉并重新创建;
# 所以, 以"w+"的方式打开文件, 总会创建新的文件, 所以如果去读, 那么读到的内容永远都是空的;
# (所以其实"w+"并没有意义)

# a+: 追加和读的方式打开文件;

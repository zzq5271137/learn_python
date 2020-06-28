"""
字符串的编码和解码
"""
from hashlib import md5

# 在Python中, 使用单引号或双引号写出来的普通字符串是unicode字符串, unicode是一个万能字符集, 可以存储任意字符,
# 但是unicode字符串只能在内存中存在, 不能存储在磁盘或者在网络中传输, (因为unicode字符串是还未进行编码的字符串);
# 如果想要将字符串存储在磁盘(存储在文件中)或者在网络中传输, 必须要将unicode字符串转换为bytes类型的字符串(即编码后的字符串),
# 一种方式是在写字符串时, 就用b"xxx"或者b'xxx'的形式, 或者, 可以使用函数进行编码和解码:
# encode('utf-8'): 将unicode字符串编码成bytes类型字符串, 编码方式采用utf-8
# decode('utf-8'): 将bytes类型字符串解码成unicode字符串, 解码方式采用utf-8
# 注: unicode是字符集, utf-8是编码方式, 其他编码方式例如: gbk、ascii等
text_normal = "hello world"
print("普通字符串类型: " + str(type(text_normal)))
text_encoded = text_normal.encode('utf-8')  # unicode -> bytes
print("编码后的字符串类型: " + str(type(text_encoded)))
print("#####################################################################")
text_bytes = b'hello world'
print("bytes字符串类型: " + str(type(text_bytes)))
text_decoded = text_bytes.decode('utf-8')  # bytes -> unicode
print("解码后的字符串类型: " + str(type(text_decoded)))

print("#####################################################################")

# 小例子: 我们使用md5对字符串进行加密时, 要求字符串的类型必须是bytes, 如果是str(unicode字符串), 则会报错
text = "hello world"
# result = md5(text).hexdigest()  # 会报错
result = md5(text.encode('utf-8')).hexdigest()
print(result)

# 小例子: 其实, 很多方法为了使用者方便, 它不要求传入的参数是经过编码的, 它会在方法内部对传进来的字符串进行编码,
# 如果你传进来编码后的字符串(bytes), 反而会报错; 比如将字符串写进文件的write()方法就会接受一个普通字符串(str)
# (因为按道理来说, 想要将字符串保存在磁盘上面, 要求字符串类型必须为bytes, 但是write()方法在底层帮你做了编码,
# 所以你只需要传入str类型字符串即可, 即具体问题具体分析)
content = "hello world"
with open("test.txt", "w") as fp:
    fp.write(content)

"""
文件的写入
"""

# write()方法
fp = open("04-file_write.txt", 'a')
fp.write('today is sunday\n')
fp.close()

# writelines()方法
fp = open("04-file_write.txt", 'a')
content = ['123\n', '456\n', '789\n']
fp.writelines(content)  # writelines()方法可以传入一个列表或是元组
fp.close()

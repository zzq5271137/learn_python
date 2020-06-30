"""
案例: 拷贝文件
"""


def copy_file_1():
    """
    先将待拷贝的文件内容读出来, 然后存储到一个中间变量中, 再将其内容写入到新文件中
    """
    lines = []
    with open("07-file_demo_1.txt", "r") as fp:
        for line in fp:
            lines.append(line)
    with open("07-file_demo_1_copy.txt", "w") as fp:
        fp.writelines(lines)


def copy_file_2():
    """
    一次性打开两个文件, 从待拷贝文件中读取内容然后直接写到新文件中
    """
    with open("07-file_demo_1.txt", "r") as fp_origin:
        with open("07-file_demo_1_copy.txt", "w") as fp_copy:
            for line in fp_origin:
                fp_copy.write(line)


copy_file_2()

"""
小案例: 打印九九乘法表
"""

row = 1
column = 1
while row < 10:
    while column <= row:
        """
        print()函数会自动换行, 想要让print()函数不换行,
        可以在打印时传入一个end参数, 即结束符, 将end设置为空字符串;
        """
        print("%s*%s=%s  " % (row, column, row * column), end='')
        column += 1
    column = 1
    row += 1
    print()

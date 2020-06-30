"""
案例: 复制图片
"""

source_path = input("请输入需要复制的图片地址: ")
dest_path = input("请输入复制的目的地: ")
with open(source_path, "rb") as fp_source:  # "rb": 以二进制的方式打开文件(读)
    with open(dest_path, "wb") as fp_dest:  # "wb": 以二进制的方式打开文件(写)
        fp_dest.write(fp_source.read())
print("图片拷贝完成")

from .. import my_request  # 两个".."表示上级目录(相对路径的方式)

print("模块my_whatever1被导入了")  # 如果你导入了某个包或模块, 那么Python会马上将那个模块中的代码立即执行一遍


def sayhello1():
    print("hello world")

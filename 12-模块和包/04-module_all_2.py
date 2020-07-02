"""
__all__变量的作用
"""

from all_test import *

"""
__all__:
1. 如果是在模块中写了这个变量, 它将控制"from 模块名 import *"的行为;
   如果不在模块中定义__all__变量, 那么"from 模块名 import *"将默认导入该模块下的所有东西;
2. 如果是在__init__.py文件中写了这个变量, 它将控制"from 包名 import *"的行为;
   如果不在包下的__init__.py中定义__all__变量, 那么"from 包名 import *"将不能导入任何模块;
__all__变量是一个列表;

此处演示2
"""

# 由于all_test/__init__.py中定义了__all__变量, 并且它包含了'all_whatever'和'all_another'这两个模块,
# 所以他们都可以使用
print("all_whatever模块内容: ")
print(all_whatever.GLOBAL_ZZQ)
all_whatever.sayhello()
p1 = all_whatever.Person()
print("###############################################")
print("all_another模块内容: ")
print(all_another.GLOBAL_ID)
all_another.sayhello2()
d1 = all_another.Dog()

"""
__all__变量的作用
"""

from all_test.all_whatever import *

# 没有写进all_whatever模块中的__all__变量的东西, 可以通过主动导入来访问
# from all_test.all_whatever import sayhello
# from all_test.all_whatever import Person

"""
__all__:
1. 如果是在模块中写了这个变量, 它将控制"from 模块名 import *"的行为;
   如果不在模块中定义__all__变量, 那么"from 模块名 import *"将默认导入该模块下的所有东西;
2. 如果是在__init__.py文件中写了这个变量, 它将控制"from 包名 import *"的行为;
   如果不在包下的__init__.py中定义__all__变量, 那么"from 包名 import *"将不能导入任何模块;
__all__变量是一个列表;

此处演示1
"""

# 由于all_test/all_whatever.py中定义了__all__变量, 并且里边只有'GLOBAL_ZZQ'这一项,
# 所以sayhello()函数和Person类都用不了了(但是我们可以主动导入他们, 然后依然可以使用,
# 只不过如果只通过"import *"的方式是访问不到的)
print(GLOBAL_ZZQ)
# sayhello()
# p1 = Person()

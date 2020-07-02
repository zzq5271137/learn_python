"""
如果是在__init__.py文件中写了这个变量, 它将控制"from 包名 import *"的行为;
如果不在包下的__init__.py中定义__all__变量, 那么"from 包名 import *"将不能导入任何模块;
"""
__all__ = ['all_whatever', 'all_another']

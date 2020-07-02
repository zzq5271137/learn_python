"""
导包的原理
"""

import sys

print("导入前, sys.modules是否包含import_principle.principle_a: %s" %
      ('import_principle.principle_a' in sys.modules))

from import_principle import principle_a
from import_principle import principle_a

"""
在执行"import xxx"或者"from xxx import xxx"的真正导入之前, Python会先判断导入的模块在sys.modules中存不存在,
如果存在, 就什么都不做, 如果不存在, 再去执行相应的导入步骤; 一旦导入了某一个模块, 比如上面导入的principle_a, 
那么Python会做3件事情:
1. 将principle_a.py这个模块添加到sys.modules这个字典中
   sys.modules这个字典的作用是, 我们有可能导入同一模块多次, 比如这里导入了两次principle_a模块,
   或者导入的那些模块中有可能会导入相同的一些其他模块(也就是导入多次), 比如, 这里导入的principle_a模块中导入了principle_b模块,
   而在principle_b模块中又导入了principle_a模块; 但是在真正导入模块前, 会先查看sys.modules这个字典中是否已经存在该模块, 
   如果已存在, 则什么都不做, 如果不存在, 才会去做这1、2、3步;
2. 执行principle_a.py中的代码
3. 在当前文件中, 创建一个变量叫做principle_a来指向这个模块
   所以这里的"from import_principle import principle_a"的principle_a, 其实是一个变量, 它指向具体模块(principle_a.py)

从某个模块中导入具体的类、方法、变量, 是相同的道理, 也会做以上3步, 只不过对于第1步, 即便你只是导入某个模块下的某个方法,
Python也会把整个模块加入到sys.modules中(sys.modules中存的是模块, 而不是具体的类、方法等); 
而对于第3步, 这个变量是指向那个模块下的具体的东西;
"""

print("导入后, sys.modules是否包含import_principle.principle_a: %s" %
      ('import_principle.principle_a' in sys.modules))

principle_a.sayhello()  # 这里的principle_a是一个指向principle_a.py的变量

print("#########################################################################")

# 其实在还没有导入模块之前, sys.modules这个字典中已经存在了很多模块, 比如os模块
print('导入os模块前, sys.modules中是否包含os模块: %s' % ('os' in sys.modules))  # True
# 但是我们不能直接使用, 因为缺少了上面的第3步, 即在当前这个文件中用一个变量指向os模块, 所以需要手动导入一下, 以让其执行第3步
import os  # 手动导入这个的目的是为了让其执行第3步

print(os.getcwd())

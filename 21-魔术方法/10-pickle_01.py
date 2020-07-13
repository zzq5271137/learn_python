"""
对象的序列化和持久化
"""

import pickle

"""
对象的序列化和持久化:
有时候, 我们想要将一个对象保存在磁盘中, 这时候我们就需要使用到对象的持久化技术了; 在Python中, 
如果要将一个对象存储到磁盘中或者从磁盘中加载一个对象, 需要使用pickle模块, pickle模块是用作对象的序列化和反序列化的; 
详细来说, 序列化:
1. pickle.dump()方法:
   将obj对象序列化为字节(bytes)写入到文件中;
2. pickle.dumps()方法:
   将obj对象序列化并返回一个bytes对象;
反序列化:
1. pickle.load()方法:
   从一个对象文件中读取序列化数据, 将其反序列化之后返回一个对象;
2. pickle.loads()方法:
   将bytes对象反序列化并返回一个对象;
(参考: https://blog.csdn.net/Darkman_EX/article/details/80752049)
Python许多内置的数据结构(对象)是可以直接序列化的, 例如: 整型、浮点型、字符串、字典、列表、元组等;
以下举几个例子来介绍序列化和持久化的大体步骤;
"""

# 将对象写入磁盘中
# 注: 这个文件的后缀名其实可以随便取, 但是因为我们使用的是pickle模块, 所以我们习惯把后缀名取成".pkl"
with open('10-pickle_01_data.pkl', 'wb') as fp:
    data = {
        'my_int': 233,
        'my_str': '你好，世界',
        'my_list': [1, 2, 3],
        'my_tuple': ('zzq', 27),
        'my_dict': {'name': 'zzq', 'id': 820064}
    }
    pickle.dump(data, fp)

# 从磁盘中加载对象
with open('10-pickle_01_data.pkl', 'rb') as fp:
    data = pickle.load(fp)
    print(data)

"""
正则表达式: 贪婪模式(greedy)与懒惰模式(lazy)
"""

import re

"""
贪婪模式(greedy): 正则表达式会匹配尽量多的字符, 默认是贪婪模式;
懒惰模式(lazy), 或者叫勉强模式(reluctant): 正则表达式会匹配尽量少的字符;

例如'+', 它是匹配1到多个字符, 最少为1个; 如果采用贪婪模式(默认), 它会匹配尽量多的字符;
如果采用懒惰模式, 它会匹配尽量少的字符, 即只匹配1个字符;
"""
text = '123456'
res = re.match('\d+', text)
print('贪婪模式的匹配结果: {}'.format(res.group()))
res = re.match('\d+?', text)  # 懒惰模式的使用: 在后面加一个'?'
print('懒惰模式的匹配结果: {}'.format(res.group()))

"""
案例: 匹配0~100之间的数字
"""

import re

"""
案例: 匹配0~100之间的数字
可以出现的数字: 1、2、10、90、100
不可以出现的数字: 09、101
"""
text = '100'
res = re.match('^[1-9]\d?$|^100$', text)
print(res.group())

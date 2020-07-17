"""
正则表达式: 以...开始、以...结尾、多表达式匹配
"""

import re

"""
'^': 表示以...开始(注意, '[]'中的'^'表示'非'或者'除了');
'&': 表示以...结束;

注: 如果使用re.match(pattern, text)函数进行匹配, 其实没有必要使用'^', 因为re.match()函数本来就是从头开始匹配,
如果第一个字符不匹配, 则视为不匹配, 也就相当于'^'的作用, 即要求text以...开始;
如果使用re.search(pattern, text)进行匹配, 则'^'有用, 因为re.search()会从text的所有位置去尝试匹配,
所以如果使用'^', 就表示要求text以...开头, 也就是从text的头部开始匹配;
"""
text = 'zzq@gmail.com'
res = re.match('^[a-z]+@[a-z]+\.com$', text)
print(res.group())

print("##################################################")

"""
'|': 匹配多个表达式或者字符串(表示'或者')
"""
text = 'https://www.baidu.com'
res = re.match('^(ftp|http|https)://www\.[a-zA-Z0-9]+\.com$', text)
print(res.group())

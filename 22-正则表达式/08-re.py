"""
re模块常用函数详解
"""

import re

"""
1. match(): 
   从开始的位置进行匹配, 如果开始的位置没有匹配到, 就直接匹配失败了;
2. search():
   会在字符串的所有位置进行尝试匹配, 如果匹配到, 就返回;
3. group()/groups():
   在正则表达式中, 可以对过滤到的字符串进行分组, 分组使用圆括号的形式;
   使用group()函数可以获得分组的匹配结果(或者获得全部的匹配结果, 取决于传入的参数):
   a). group()和group(0)是等价的, 返回的是整个字符串的匹配结果, 因为它会将整个正则表达式视为一个大的分组,
       即相当于将整个正则表达式用圆括号包起来作为一个分组;
   b). group(1)、group(2)...返回的是第1、2...个圆括号内的(即分组的)匹配结果;
   c). group(1, 2)返回的是第1、2个圆括号内的(即分组的)匹配结果, 是一个元组;
   d). groups()返回的是匹配的所有分组, 是一个元组;
"""
text = 'apple price is $99, orange price is $78'
res = re.search(r'.*(\$\d+).*(\$\d+)', text)
print(res.group())
print(res.group(0))
print(res.group(1))
print(res.group(2))
print(res.group(1, 2))
print(res.groups())

print("#################################################################")

"""
4. finalall():
   找出所有匹配的字符串, 全部返回回来, 返回的是一个列表;
"""
text = 'apple price is $99, orange price is $78'
res = re.findall('\$\d+', text)
print(res)

print("#################################################################")

"""
5. sub():
   用来替换字符串, 将匹配到的字符串替换为其他字符串;
"""
text = 'apple price is $99, orange price is $78'
res = re.sub('\$\d+', '0', text)
print(res)

print("#################################################################")

"""
6. split():
   使用正则表达式来分割字符串;
"""
text = 'hello world&ni hao'
res = re.split('[^a-zA-Z]', text)  # 将非英文字符的字符都作为分隔符
print(res)

print("#################################################################")

"""
7. compile():
   对于一些经常要用到的正则表达式, 可以使用compile()函数进行编译并存在内存中, 后期再使用的时候可以直接拿过来用,
   执行效率会更快; 而且compile()函数还可以指定flags=re.VERBOSE, 在写正则表达式的时候可以做好注释;
"""
text = 'the number is 20.50'
r = re.compile(r'''
\d+  # 小数点前面的数字
\.?  # 小数点
\d*  # 小数点后面的数字
''', flags=re.VERBOSE)
res = re.search(r, text)
print(res.group())

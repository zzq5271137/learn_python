"""
将字典转化为XML, 并写入文件
"""

import dicttoxml
from xml.dom.minidom import parseString

"""
需要时用第三方的库, dicttoxml:
    pip install dicttoxml
"""

people_dict = [
    'Class 01',
    3,
    {'name': '挣命1', 'age': 27, 'salary': 15000},
    {'name': '挣命2', 'age': 28, 'salary': 25000},
    {'name': '挣命3', 'age': 29, 'salary': 35000}
]

# 将字典转换为XML字符串(bytes类型)
print('###########将字典转换为XML字符串(bytes类型)###########')
people_bxml = dicttoxml.dicttoxml(people_dict, custom_root='people')
print(people_bxml)
print()

# 将bytes类型使用utf-8解码为str类型(因为有中文)
print('###########将bytes类型使用utf-8解码为str类型(因为有中文)###########')
people_xml = people_bxml.decode('utf-8')
print(people_xml)
print()

# 解析XML字符串, 生成带有缩进格式的版本
print('###########解析XML字符串, 生成带有缩进格式的版本###########')
people_dom_obj = parseString(people_xml)
people_xml_pretty = people_dom_obj.toprettyxml(indent=' ' * 4)
print(people_xml_pretty)

# 将解析后的XML内容写进文件
print('###########将解析后的XML内容写进文件###########')
with open('files/people.xml', 'w') as fp:
    fp.write(people_xml_pretty)
print('Done.')

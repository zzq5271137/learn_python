"""
读取与检索XML文件
"""

from xml.etree.ElementTree import parse

doc = parse('files/products.xml')

for item in doc.iterfind('products/product'):
    id = item.findtext('id')
    name = item.findtext('name')
    price = item.findtext('price')
    uuid = item.get('uuid')
    print("Product(uuid={}, id={}, name={}, price={})".format(uuid, id, name, price))

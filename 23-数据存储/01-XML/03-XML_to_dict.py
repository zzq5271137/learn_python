"""
从XML文件中读取内容, 并转化为字典
"""

import xmltodict

"""
需要时用第三方的库, xmltodict:
    pip install xmltodict
"""

with open('files/products.xml', 'r', encoding='utf-8') as fp:
    # 读取XML文件
    products_xml = fp.read()

    # 将读取出的XML文件内容解析成字典
    products_dict = xmltodict.parse(products_xml)
    product_list = products_dict['root']['products']['product']
    print(type(product_list))
    for p in product_list:
        print("Product(uuid={}, id={}, name={}, price={})".format(p['@uuid'], p['id'], p['name'],
                                                                  p['price']))

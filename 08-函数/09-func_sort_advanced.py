"""
sort()方法和sorted()函数的高级用法
"""

from functools import cmp_to_key

# 对简单的数值类型进行排序
numbers = [6, 3, 1, 4, 5, 2]
print("before sort: %s" % numbers)
numbers.sort(reverse=True)  # 可降序
print("after sort: %s" % numbers)

print("##########################################")

# 对字典进行排序(想要有自己的排序规则, 需要自己定义cmp()函数, 然后传入到sort()方法中)
people = [
    {
        "name": "zzq",
        "age": 35
    },
    {
        "name": "zhangsan",
        "age": 20
    },
    {
        "name": "lisi",
        "age": 20
    }
]


# 对于cmp()函数: 我们约定, 如果返回的值大于0, 则代表a > b; 如果返回的值小于0, 则代表a < b;
# 如果返回的值等于0, 则代表a与b相等; (类似于Java中的compareTo()方法)
def my_cmp(a, b):
    """
    自定义的cmp()函数, 可以根据自己的需求进行比较(比如这里, 先比较age, age相等的话再比较name)
    :param a: 待比较的字典a
    :param b: 待比较的字典b
    :return: 比较结果
    """
    if a['age'] > b['age']:
        return 1
    elif a['age'] < b['age']:
        return -1
    else:
        if a['name'] > b['name']:
            return 1
        else:
            return -1


print("before sort: %s" % people)
people.sort(key=cmp_to_key(my_cmp))  # 传入我们自定义的比较函数
print("after sort: %s" % people)

print("################################################################################")

# 对于sorted()函数, 也可以这么用
# (记得sorted()函数与sort()方法的区别在于, sort()方法是由一个列表去调用的, 它会改变原有列表;
# sorted()函数是直接调用的, 传入一个列表作为参数, 它不会改变原有列表, 而是会生成一个新的列表)
people = [
    {
        "name": "zzq",
        "age": 35
    },
    {
        "name": "zhangsan",
        "age": 20
    },
    {
        "name": "lisi",
        "age": 20
    }
]
print("before sorted: people={}".format(people))
people_sorted = sorted(people, key=cmp_to_key(my_cmp))  # 传入我们自定义的比较函数
print("after sorted: people={}, people_sorted={}".format(people, people_sorted))

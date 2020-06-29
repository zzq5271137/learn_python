"""
函数式编程练习
"""

from functools import reduce

# 使用filter()函数, 过滤掉小于3的数
nums = [1, 2, 3, 4, 5, 6]
print("before filter: nums={}".format(nums))
nums_filtered = filter(lambda x: x > 3, nums)
print("after filter: nums={}, nums_filtered={}".format(nums, list(nums_filtered)))

print("#########################################################")

# 使用map()函数, 将列表中的每个数翻三倍
nums = [1, 2, 3, 4, 5, 6]
print("before map: nums={}".format(nums))
nums_mapped = map(lambda x: x * 3, nums)
print("after map: nums={}, nums_mapped={}".format(nums, list(nums_mapped)))

print("#########################################################")

# 使用reduce()函数, 求列表中的数值之和
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reduce(lambda x, y: x + y, nums))

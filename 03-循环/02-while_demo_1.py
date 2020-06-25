"""
小案例: 计算1~100数值之和
"""

res = 0
index = 1
while index <= 100:
    res += index
    index += 1
print("1~100数值之和: " + str(res))

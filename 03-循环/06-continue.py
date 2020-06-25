"""
continue: 跳过当前这一次循环
"""

index = 0
while index < 10:
    index += 1
    if index == 5:
        continue
    print(index)

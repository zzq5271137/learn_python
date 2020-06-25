"""
小案例: 打印1~10所有奇数
"""

num = 1
while num <= 10:
    if num % 2 == 0:
        num += 1
        continue
    print(num)
    num += 1

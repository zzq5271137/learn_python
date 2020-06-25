"""
小案例: 猜数字小游戏
"""

target = 37
input_value = int(input("请输入数字: "))
while input_value != target:
    if input_value < target:
        input_value = int(input("输入的数字小了, 请再次输入: "))
    elif input_value > target:
        input_value = int(input("输入的数字大了, 请再次输入: "))
print("正确！")

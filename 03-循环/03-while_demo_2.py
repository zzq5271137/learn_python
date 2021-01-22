"""
小案例: 猜数字小游戏
"""

target = 37

while True:
    try:
        input_value = int(input("enter: "))
        if input_value == target:
            print("bingo!")
            break
        if input_value < target:
            print("need be larger")
        if input_value > target:
            print("need be smaller")
    except Exception as e:
        print("wrong input, try again")
        continue

"""
案例: 计算器
"""


def calculator(option):
    operator = None
    if option == 1:
        def add(x, y):
            return x + y

        operator = add
    elif option == 2:
        def minus(x, y):
            return x - y

        operator = minus
    elif option == 3:
        def multiply(x, y):
            return x * y

        operator = multiply
    else:
        def divide(x, y):
            return x / y

        operator = divide

    return operator


cal = calculator(1)
print(cal(2, 3))
cal = calculator(2)
print(cal(2, 3))
cal = calculator(3)
print(cal(2, 3))
cal = calculator(4)
print(cal(2, 3))

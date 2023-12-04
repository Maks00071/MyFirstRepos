# функция деления
def division_func(x: int, y: int):
    try:
        return x / y
    except ZeroDivisionError:
        return "Division by Zero!!!"


print(division_func(3, 3))
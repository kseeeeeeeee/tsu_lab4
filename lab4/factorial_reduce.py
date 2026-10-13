
from functools import reduce


def factorial(number):
    if number < 0:
        raise ValueError("Число должно быть неотрицательным")

    return reduce(lambda x, y: x * y, range(1, number + 1), 1)


number = int(input("Введите целое неотрицательное число: "))

print("Факториал числа", number, "равен", factorial(number))

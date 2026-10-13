
def filter_positive(numbers):
    return filter(lambda number: number > 0, numbers)


def square_numbers(numbers):
    return map(lambda number: number ** 2, numbers)


def filter_greater_than_ten(numbers):
    return filter(lambda number: number > 10, numbers)


def pipeline(numbers):
    result = filter_positive(numbers)
    result = square_numbers(result)
    result = filter_greater_than_ten(result)
    return list(result)


numbers = [-3, -1, 0, 2, 3, 4, 5]

print("Исходный список:", numbers)
print("Результат обработки:", pipeline(numbers))

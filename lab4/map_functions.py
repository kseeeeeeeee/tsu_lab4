
numbers = [1, 2, 3, 4, 5]

functions = [
    lambda x: x * 2,
    lambda x: x ** 2,
    lambda x: x + 10
]

for function in functions:
    result = list(map(function, numbers))
    print(result)

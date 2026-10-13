
def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def prime_generator(limit):
    number = 2

    while number <= limit:
        if is_prime(number):
            yield number

        number += 1


limit = int(input("Введите верхнюю границу: "))

print("Простые числа:", list(prime_generator(limit)))


class NumberIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        number = self.current
        self.current += 1
        return number


start = int(input("Введите начальное число: "))
end = int(input("Введите конечное число: "))

for number in NumberIterator(start, end):
    print(number)

def analyze(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0
    for num in numbers:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
        total += num
    average = total / len(numbers)
    return minimum, maximum, average

numbers = [5, 12, 8, 21, 34, 17, 9, 44, 3, 27]

mn, mx, avg = analyze(numbers)

print("Минимальное значение:", mn)
print("Максимальное значение:", mx)
print("Среднее арифметическое:", avg)

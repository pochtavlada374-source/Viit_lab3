def calculate_average(measurements):
    total = 0
    for value in measurements:
        total += value
    return total / len(measurements)

def find_minimum(measurements):
    minimum = measurements[0]
    for value in measurements:
        if value < minimum:
            minimum = value
    return minimum

def find_maximum(measurements):
    maximum = measurements[0]
    for value in measurements:
        if value > maximum:
            maximum = value
    return maximum

def count_above_average(measurements):
    average = calculate_average(measurements)
    count = 0
    for value in measurements:
        if value > average:
            count += 1
    return count

def find_value(measurements, target):
    for index, value in enumerate(measurements):
        if value == target:
            return index
    return -1

def analyze_measurements(measurements):
    return find_minimum(measurements), find_maximum(measurements), calculate_average(measurements)

measurements = [12.5, 8.3, 15.1, 9.7, 22.4, 6.8, 18.9, 11.2, 14.6, 10.0]

count = len(measurements)
minimum, maximum, average = analyze_measurements(measurements)
above_average = count_above_average(measurements)

print("Количество измерений:", count)
print("Минимальное значение:", minimum)
print("Максимальное значение:", maximum)
print("Среднее значение:", average)
print("Количество значений выше среднего:", above_average)

target = float(input("Введите значение для поиска: "))
index = find_value(measurements, target)
if index != -1:
    print(f"Значение {target} найдено на позиции {index} (индекс {index})")
else:
    print(f"Значение {target} в наборе отсутствует")

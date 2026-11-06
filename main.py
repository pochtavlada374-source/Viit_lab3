measurements = (7, 5, 6, 9, 12, 4, 2, 1)

temp_list = list(measurements)
temp_list[0] = 10
print("Количество элементов:", len(temp_list))
print("Сумма элементов:", sum(temp_list))
print("Минимальное значение:", min(temp_list))
print("Максимальное значение:", max(temp_list))
print("Среднее арифметическое:", sum(temp_list) / len(temp_list))

sorted_copy = sorted(temp_list)
print("Копия:", sorted_copy)

temp_list.sort()
print("Список после .sort():", temp_list)

numbers = [-10, 3, -2, 8, -5]

sorted_default = sorted(numbers)
print("Обычная сортировка:", sorted_default)
sorted_abs = sorted(numbers, key=lambda x: abs(x))
print("Сортировка Key:", sorted_abs)

measurements = (7, 5, 6, 9, 12, 4, 2, 1)

first, second = measurements[0], measurements[1]
print("first =", first)      # 3.5
print("second =", second)    # 7.2

mens_list = list(measurements)
mens_list[0] = 10
measurements = tuple(mens_list)
print("Изменённый кортеж:", measurements)

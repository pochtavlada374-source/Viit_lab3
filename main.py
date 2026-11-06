numbers = [7, 6, 10, 54, 8, 3, 5, 1, 9, 17, 71]

print("1st element:", numbers[0])
print("3st element:", numbers[2])
print("last element:", numbers[-1])

numbers[1] = 100

numbers.append(50)

numbers.remove(8)

print("Итоговый список:", numbers)
print("Количество элементов:", len(numbers))
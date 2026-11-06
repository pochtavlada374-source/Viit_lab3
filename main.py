def find_element(numbers, target):
    for index, value in enumerate(numbers):
        if value == target:
            return index
    return -1

numbers = [10, 20, 12, 3, 4, 61, 34, 100]

print(find_element(numbers, 34))
print(find_element(numbers, 13))
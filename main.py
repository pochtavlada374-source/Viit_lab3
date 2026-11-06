def greet(name):
    print(f"Привет, {name}!")

def square(number):
    return number ** 2

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

greet("VLAD")
greet("SASHA")
print(square(3))
print(square(12)) 
print(max_of_two(7, 15))
print(max_of_two(-23, -123))
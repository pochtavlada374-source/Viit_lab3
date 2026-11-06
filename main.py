def calculate_rectangle(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

def describe_rectangle(width, height, unit="см"):
    S = calculate_rectangle(width, height)
    P = calculate_perimeter(width, height)
    print(f"Прямоугольник: ширина = {width} {unit}, высота = {height} {unit}")
    print(f"Площадь: {S} {unit} кв")
    print(f"Периметр: {P} {unit}")

print("Вызов без аргумента unit")
describe_rectangle(5, 3)

print("\n Вызов с аргументом unit")
describe_rectangle(17, 3, unit="м")
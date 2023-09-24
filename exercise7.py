import math

print("Выберите фигуру для вычисления площади:")
print("1 - Прямоугольник")
print("2 - Треугольник")
print("3 - Круг")

choice = int(input("Введите номер фигуры: "))

if choice == 1:
    width = float(input("Введите ширину прямоугольника: "))
    height = float(input("Введите высоту прямоугольника: "))
    area = width * height
    print("Площадь прямоугольника равна:", area)
elif choice == 2:
    base = float(input("Введите основание треугольника: "))
    height = float(input("Введите высоту треугольника: "))
    area = 0.5 * base * height
    print("Площадь треугольника равна:", area)
elif choice == 3:
    radius = float(input("Введите радиус круга: "))
    area = math.pi * radius ** 2
    print("Площадь круга равна:", area)
else:
    print("Ошибка: неверный выбор фигуры")
distance = int(input("Введите дальность выстрела: "))

if distance > 28 and distance < 30:
    print("ПОПАЛ")
elif distance >= 30:
    print("ПЕРЕЛЕТ")
elif distance > 0 and distance <= 28:
    print("НЕДОЛЕТ")
else:
    print("НЕ БЕЙ ПО СВОИМ")
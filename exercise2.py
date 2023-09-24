a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a == b or a == c or b == c:
    print("Ошибка: среди чисел есть равные")
else:
    if a > b:
        if b > c:
            middle = b
        elif a > c:
            middle = c
        else:
            middle = a
    else:
        if a > c:
            middle = a
        elif b > c:
            middle = c
        else:
            middle = b
    print("Среднее из трех чисел:", middle)
    
    average = (a + b + c) / 3
    print("Среднее арифметическое из трех чисел:", average)
    #я не уверена, что зчначит среднее - среднее из трих чисел, или просто среднее арифметичесое, поэтому сделала и то и то
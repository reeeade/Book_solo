a = eval(input("Введите значение А: "))
b = eval(input("Введите значение B: "))
eq = "Ax = B - A - 1"
if a != 0:
    x = (b - 1) / a - 1
    print(f"Уравнение {eq} иммеет корень x = {round(x, 2)}")
else:
    if b == 1:
        print("Решение - любое число")
    else:
        print("Решений нет")

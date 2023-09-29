try:
    a = eval(input("Введите первое число: "))
    b = eval(input("Введите второе число: "))
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        print('Первое число больше') if a > b else print('Второе число больше')
    else:
        print("Не вводите буквы/символы")
except SyntaxError:
    print("Введите число!")
except NameError:
    print("Нельзя вводить символы и буквы!")

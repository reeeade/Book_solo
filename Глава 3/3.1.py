inp = tuple(input("Введите текст: "))
inp_len = int(input("Введите расстояие между элементами кортежа: "))
new_tuple = inp[::inp_len]
print(new_tuple)
num = int(input("Введите целое число: "))
new_tuple = tuple(int(i) for i in str(num))
revers_tuple = new_tuple[::-1]
print(new_tuple)
print(revers_tuple)
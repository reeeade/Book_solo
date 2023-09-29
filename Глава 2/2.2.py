num = int(input("Введите целое число: "))
new_digit =''
for digit_str in str(num):
    digit = int(digit_str)
    new_digit += str(9 - digit)

print(f"Новое число: {new_digit}")

num = int(input("Введите целое число: "))
num_list = [0] * 10
for digit_str in str(num):
    digit = int(digit_str)
    num_list[digit] += 1
print(num_list)
for digit in range(10):
    count = num_list[digit]
    if count > 0:
        print(f"Цифра {digit} встречается в числе {num} {count} раз(а)")

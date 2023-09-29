inp_list = eval(input("Введите список натуральных чисел: "))
new_num = ''
for digit in inp_list:
    new_num += str(digit)
print(new_num)

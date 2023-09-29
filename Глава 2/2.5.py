inp_list = eval(input("Введите список натуральных чисел: "))
inp_range = int(input("Введите верхню границу суммы: "))
sum_list = 0
for num in range(inp_range + 1):
    if num not in inp_list:
        sum_list += num
print(sum_list)

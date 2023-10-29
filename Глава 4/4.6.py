num = int(input("Введите число: "))
keys_list = [i for i in range(1, num + 1)]
value_list = list(reversed(keys_list))
new_dict = dict(zip(keys_list, value_list))
print(new_dict)
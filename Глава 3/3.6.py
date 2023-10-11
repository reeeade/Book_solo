new_list = [5, 3, 9, 1, 7, 4, 2, 8, 5, 2]
how_much = int(input("Введите число переборов: "))
for k in range(how_much):
    for i in range(len(new_list) - 1):
        if new_list[i] > new_list[i + 1]:
            new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
print(new_list)

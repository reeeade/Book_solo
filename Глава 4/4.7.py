txt = input("Введите текст: ")
new_dict = {}
for i in txt:
    new_dict[i] = new_dict.get(i, 0) + 1
print(new_dict)
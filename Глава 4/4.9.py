txt = input("Введите текст: ")
new_dict = {}
for i in range(len(txt)):
    new_dict[txt[i]] = new_dict.get(txt[i], txt[:i] + txt[i + 1:])

print(new_dict)
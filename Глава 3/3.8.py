from random import randint as ri

len_list = 10
new_list = [ri(1, 20) for i in range(len_list)]
print("Список из случайных чисел:", new_list)
chet_list = sorted([new_list[i] for i in range(len_list) if i % 2 == 0])
print("Лист четных элементов в порядке возрастания:", chet_list)
nechet_list = sorted([new_list[i] for i in range(len_list) if i % 2 != 0], reverse=True)
print("Лист нечетных элементов в порядке убывания:", nechet_list)

sorted_list = []
chet_ind, nechet_ind = 0, 0

for i in range(len_list):
    if i % 2 == 0:
        sorted_list.append(chet_list[chet_ind])
        chet_ind += 1
    else:
        sorted_list.append(nechet_list[nechet_ind])
        nechet_ind += 1
print(sorted_list)

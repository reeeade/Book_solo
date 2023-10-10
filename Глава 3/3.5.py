from random import randint as ri

matrix = [[ri(0, 9) for j in range(5)] for i in range(5)]
for i in matrix:
    print(i)
print("-----------")

del_i = int(input("Введите номер строки для удаления: "))
matrix.pop(del_i)

for i in matrix:
    print(i)

del_j = int(input("Введите номер столбца для удаления: "))
for i in matrix:
    i.pop(del_j)

for i in matrix:
    print(i)

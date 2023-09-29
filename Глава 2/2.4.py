list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
len1 = len(list1)
len2 = len(list2)

if len1 != len2:
    print("Длина списков не совпадает!")
else:
    for i in range(len1):
        if list1[i] != list2[i]:
            print("Элементы списков не равны!")
            break
    else:
        print("Списки равны!")

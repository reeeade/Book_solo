from random import randint as ri

rand_len = ri(8, 12)
list1 = [ri(1, 20) for i_1 in range(rand_len)]
list2 = [ri(1, 20) for i_2 in range(rand_len)]
print(list1, list2, sep="\n")
list3 = []

for i in range(rand_len):
    list3.append(list1[i])
    list3.append(list2[i])
print(list3)
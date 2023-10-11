def maxindex(lis):
    new_list = [max(lis), lis.index(max(lis))]
    return new_list


list1 = [1, 5, 6, 9, 2, 5]
print(maxindex(list1))

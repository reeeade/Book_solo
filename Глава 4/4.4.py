set3 = {i for i in range(51) if i % 3 == 0}
set4 = {i for i in range(51) if i % 4 == 0}
new_set = set3 ^ set4
print(new_set)
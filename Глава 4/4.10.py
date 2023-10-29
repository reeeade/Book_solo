from random import randint

dict_a = {randint(1, 10): randint(20, 40) for _ in range(10)}
dict_b = {randint(1, 10): randint(20, 40) for _ in range(10)}
dict_c = {}
for k in dict_a.keys() & dict_b.keys():
    _set = {dict_a[k], dict_b[k]}
    dict_c[k] = _set
print(dict_c)
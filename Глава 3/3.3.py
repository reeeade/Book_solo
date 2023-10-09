# 65
# 90
from random import randint as ri


def create_list(i, j):
    new_list = [[chr(ri(65, 90)) for a in range(i)] for b in range(j)]
    print(new_list)


create_list(4, 3)

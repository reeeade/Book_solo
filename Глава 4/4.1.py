from random import randint

new_set = set()
while len(new_set) < 5:
    new_set.add(randint(1, 10))
while len(new_set) < 15:
    new_set.add((randint(11, 30)))
print(new_set)
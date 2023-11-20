s = 5
while s != 0:
    if s != 3:
        print(f'{"*":>{s}}', end='')
        print(" " * (2 * (5 - s)), end='')
        print(f'{"*":<{s}}')
    else:
        print(f'{"*":>{s}}', end='')
        print("*" * (2 * (5 - s)), end='')
        print(f'{"*":<{s}}')
    s -= 1

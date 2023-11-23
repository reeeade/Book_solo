def coding(txt):
    f_1 = ord("а")
    f_2 = ord("А")
    l_1 = ord("я")
    l_2 = ord("Я")
    new_txt = ''
    for s in txt:
        k = ord(s)
        if f_1 + 1 < k <= l_1 or f_2 + 1 < k <= l_2:
            s = chr(k - 2)
        elif k == f_1 + 1:
            s = chr(l_1)
        elif k == f_2 + 1:
            s = chr(l_2)
        elif k == f_1:
            s = chr(l_1 - 1)
        elif k == f_2:
            s = chr(l_2 - 1)
        new_txt += s
    return new_txt


def decoding(txt):
    f_1 = ord("а")
    f_2 = ord("А")
    l_1 = ord("я")
    l_2 = ord("Я")
    new_txt = ''
    for s in txt:
        k = ord(s)
        if f_1 <= k < l_1 - 1 or f_2 <= k < l_2 - 1:
            s = chr(k + 2)
        elif k == l_1:
            s = chr(f_1 + 1)
        elif k == l_2:
            s = chr(f_2 + 1)
        elif k == l_1 - 1:
            s = chr(f_1)
        elif k == l_2 - 1:
            s = chr(f_2)
        new_txt += s
    return new_txt


inp = input("Введите текст:")
coding_txt = coding(inp)
print(coding_txt)
print(decoding(coding_txt))

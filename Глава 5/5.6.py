inp_txt = input("Введите текст для расшифровки:")
new_txt = ''
first = ord("а")
First = ord("А")
last = ord("я")
Last = ord("Я")
for s in inp_txt:
    k = ord(s)
    if (first < k <= last) or (First < k <= Last):
        s = chr(k - 1)
    elif k == first:
        s = chr(last)
    elif k == First:
        s = chr(Last)
    new_txt += s

print(new_txt)

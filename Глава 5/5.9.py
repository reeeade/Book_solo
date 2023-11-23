inp_txt = input("ВВедите текст:")
txt_list = inp_txt.split()
# max_len = max(txt_list, key=len)
# min_len = min(txt_list, key=len)
max_len = txt_list[0]
min_len = txt_list[0]
for word in txt_list:
    if word < min_len:
        min_len = word
    elif word > max_len:
        max_len = word
txt_list.remove(max_len)
txt_list.remove(min_len)
print(' '.join(txt_list))

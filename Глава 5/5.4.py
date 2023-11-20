txt = input("input some text")
new_txt = ''
i = 0
while i < len(txt) - 2:
    new_txt += txt[i + 2] + txt[i + 1] + txt[i]
    i += 3
dif = len(txt)-len(new_txt)
if dif == 1:
    new_txt += txt[i]
elif dif == 2:
    new_txt += txt[i] + txt[i+1]
print(new_txt)

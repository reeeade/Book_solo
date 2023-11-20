txt = input("input some text:")
new_txt = ''
for s in txt:
    if s.islower():
        new_txt += chr(ord(s) - 32)
    elif s.isupper():
        new_txt += chr(ord(s) + 32)
print(new_txt)

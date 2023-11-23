text1 = input("First text:")
text2 = input("Second text:")
new_text = ''

for i in range(max(len(text1), len(text2))):
    msg1 = text1[i] if i in range(len(text1)) else '*'
    msg2 = text2[i] if i in range(len(text2)) else '*'
    new_text += msg1 + msg2
print(new_text)

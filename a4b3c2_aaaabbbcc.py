s = 'a4b3c2'
s1 = ''
for i in s:
    if i.isalpha():
        x = i
    else:
        d = int(i)
        s1 = s1 + x*d
print(s1)


    

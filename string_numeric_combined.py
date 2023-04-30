s = 'B4ALD3'
print(sorted(s))
alphabets = []
digits = []
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)
print(alphabets)
print(digits)
#The return type of sorted function is list
q = []
alphabets = sorted(alphabets)
digits = sorted(digits)
q = alphabets + digits
k = ''
k = ''.join(q)
print(k)




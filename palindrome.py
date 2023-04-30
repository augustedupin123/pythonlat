n = input("enter the string")
s = 0
sa = ""

for i in n:
    s = s + 1
for i in range(1, s+1):
    sa = sa + n[s-i]
if (n==sa):
    print('palindrome')
else:
    print('not palindrome')

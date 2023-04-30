str = input("Enter first string")
str1 = input("Enter second string")

a = str.split()
b = str1.split()
s = []

for i in a:
    if i in b:
        s.append(i)
print(s)


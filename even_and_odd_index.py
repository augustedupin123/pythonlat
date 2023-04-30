s = 'learning python is very easy'
s1 = []
s2 = []
# for i in range(1,len(s),2):
#     print(s1.append(s[i]))
# print(s1)
# below for printing even characters
for i in range(1,len(s),2):
    s1.append(s[i])
print(s1)


# below for printing odd characters
for i in range(0,len(s),2):
    s2.append(s[i])
print(s2)

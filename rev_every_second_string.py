s1 = 'one two three four five six'
s2 = s1.split()
s3 = []
print(s2)
# for i in range(0,len(s2),2):
#     s3.append(s2[i])
for i in range(0,len(s2)):
    if (i%2!=0):
        s3.append(s2[i][::-1])
    else:
        s3.append(s2[i])
print(s3)





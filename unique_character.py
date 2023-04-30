str1 = 'leetcode'
f = 0
q = 0
unique = ""
for i in range(len(str1)):
    q = 0
    for j in range(len(str1)):
        if str1[i]==str1[j]:
            q = q+1
    if q==1:
        print(str1[i])


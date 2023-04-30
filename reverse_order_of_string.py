s = 'learning python is very easy'
k = s.split()[::-1]
print(k)

s1 = 'learning python is very easy'
k1 = s1.split()
k2 = k1[::-1]
print(k2)

k3 = []
for i in k2:
    k3.append(i[::-1])
print(k3)






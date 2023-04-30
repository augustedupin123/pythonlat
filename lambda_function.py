prac_list = [123,23,234,435,346,6756,4567,45727,257]
prac_list1 = list(map(lambda x: x*2, prac_list))
print(prac_list1)


def sq(a):
    return a*a
def cube(a):
    return a*a*a
list1 = [sq,cube]
for i in range(5):
    val = list(map(lambda x:x(i), list1))
print(val)
